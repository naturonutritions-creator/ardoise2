import Image from "next/image";

export default function Logo({ className = "h-8 w-8" }: { className?: string }) {
  return (
    <Image
      src="/images/logo-cap-reussite.png"
      alt="Cap Réussite"
      width={96}
      height={96}
      className={`${className} rounded-full object-contain`}
      priority
    />
  );
}
