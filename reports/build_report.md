# Build Report

Generated: 2026-07-02

- Source route count: 81
- Public source route count: 80
- Existing build output route files: 82
- Cloudflare output directory exists: True

## Package Scripts

| Script | Command |
| --- | --- |
| build | python tools/build-cloudflare-preview.py |
| import:google-reviews | node scripts/import-google-reviews.mjs |
| import:social-gallery | node scripts/import-meta-gallery.mjs |
| build:cloudflare | python tools/build-cloudflare-preview.py |
| build:production | node -e "process.env.SUNRAY_SITE_BASE_URL='https://www.sunray-cleaning.com';process.env.SUNRAY_ALLOW_INDEXING='1';require('child_process').spawnSync('python',['tools/build-cloudflare-preview.py'],{stdio:'inherit',env:process.env});" |
| deploy:preview | npx wrangler pages deploy cloudflare-preview --project-name sunray-cleaning-preview |
| deploy:production | npm run build:production && npx wrangler pages deploy cloudflare-preview --project-name sunray-cleaning-staging --branch main |
| check:internal-links | python seo-automation/scripts/run_internal_link_check.py --root cloudflare-preview |
| reports:generate | python tools/generate-repository-intelligence.py |

## Page Build Simulation Errors

No rows.
