import { defineConfig } from 'vite';

export default defineConfig({
    server: {
        proxy: {
            '/api': 'http://localhost:8000',  // Adjust URL for production
        },
    },
});
