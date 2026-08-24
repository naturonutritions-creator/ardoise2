import { NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { db, schema } from "@/lib/db";
import { and, eq } from "drizzle-orm";

export async function POST(request: Request, context: { params: Promise<{ slug: string }> }) {
  await context.params; // le slug du quiz est informatif ; la progression est indexée par leçon
  const session = await getServerSession(authOptions);
  const { lessonSlug, score } = (await request.json()) as { lessonSlug: string; score: number };

  if (!session?.user) {
    return NextResponse.json({ message: "Connecte-toi pour enregistrer ta progression." }, { status: 401 });
  }

  const userId = Number((session.user as { id?: string }).id);

  try {
    const [existing] = await db
      .select()
      .from(schema.progressions)
      .where(and(eq(schema.progressions.userId, userId), eq(schema.progressions.lessonSlug, lessonSlug)))
      .limit(1);

    if (existing) {
      await db
        .update(schema.progressions)
        .set({
          lessonDone: true,
          quizScore: score,
          quizAttempts: existing.quizAttempts + 1,
          updatedAt: new Date(),
        })
        .where(eq(schema.progressions.id, existing.id));
    } else {
      await db.insert(schema.progressions).values({
        userId,
        lessonSlug,
        lessonDone: true,
        quizScore: score,
        quizAttempts: 1,
      });
    }

    return NextResponse.json({ message: "Progression enregistrée." });
  } catch {
    return NextResponse.json(
      { message: "Base de données non configurée sur cette démo : score non persisté." },
      { status: 503 }
    );
  }
}
