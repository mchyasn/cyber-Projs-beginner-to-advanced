/// <reference types="vite/client" />

interface ImportMetaEnv {
    readonly VITE_BACKEND_URL: string;
    readonly VITE_CHAT_URL: string;
    readonly VITE_IMAGES_URL: string;
}

interface ImportMeta {
    readonly env: ImportMetaEnv;
}