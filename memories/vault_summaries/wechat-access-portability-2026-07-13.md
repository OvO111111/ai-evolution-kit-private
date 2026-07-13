# WeChat Access Portability Correction

## Conclusion

The prior export restored instructions, not capability. It copied `SKILL.md` files
without installing the Camoufox reader runtime, pinning compatible dependencies,
or proving that a fresh machine could extract article body text. It also allowed a
single Chrome/tool denial to be described as a permanent URL/domain failure.

## Adopted Strategy

- Keep denials scoped to the attempted tool/action.
- Install the public WeChat reader and isolated venv during bootstrap.
- Pin upstream revision `69de9e413cca3fe6b770c40a4dec204afd5b2b3c` and tested dependency versions.
- Require a real Camoufox page creation smoke, then a live article body extraction.
- Recover automatically from captured debug HTML if upstream parsing fails.
- Audit user-editable local denial rules without altering or bypassing product policy.

## Evidence

- Baseline existing environment read the test article: 14,507 characters.
- First fresh-install test failed despite successful package installation because
  `playwright 1.61` was incompatible with `camoufox 0.4.11`.
- After dependency pinning, a new temporary checkout and venv created a Camoufox
  page and extracted the same 14,507-character body; temporary files were removed.
- `verify_portable_capabilities.ps1 -WechatUrl ...`: passed.
- `public_wechat_article` fresh route eval: 1/1 passed, no degraded result.
- Evolution contracts: 41/41 passed.
- Export safety scan: 294 files, 0 findings.

## Residual Boundaries

- Browser login state, cookies, and private content are not portable through GitHub.
- A future WeChat anti-bot change can still break one route; the router must continue
  to another supported route and report concrete evidence.
- Product safety policy is not bypassed or edited by these scripts.
