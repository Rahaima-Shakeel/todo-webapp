import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* existing config options here */
  images: {
    domains: ["cdn.dribbble.com"], // allow external images from this domain
  },
};

export default nextConfig;
