# CVEs

CVEs I have found, with the proof-of-concept code that goes with them.

Each one lives in its own `CVE-YYYY-NNNNN/` directory: the advisory in `README.md`, the PoC in `poc/`.

## Published

<!-- cves-table:start -->
| CVE | Product | Class | Severity | PoC |
|-----|---------|-------|----------|-----|
| [CVE-2026-100389](CVE-2026-100389/README.md) | GestSup | Unrestricted file upload | Critical | [poc](CVE-2026-100389/poc) |
| [CVE-2026-102372](CVE-2026-102372/README.md) | GestSup | Stored XSS | Medium | [poc](CVE-2026-102372/poc) |
| [CVE-2026-102373](CVE-2026-102373/README.md) | GestSup | IDOR | High | [poc](CVE-2026-102373/poc) |
| [CVE-2026-102374](CVE-2026-102374/README.md) | GestSup | Stored XSS | Medium | [poc](CVE-2026-102374/poc) |
<!-- cves-table:end -->

## Disclosure

Vendors are notified first. Nothing is published here before a fix is available or the disclosure deadline has passed.

## Using the PoCs

Published for educational purposes only, so defenders can check whether they are affected. Run them only against systems you own or are authorized to test.
