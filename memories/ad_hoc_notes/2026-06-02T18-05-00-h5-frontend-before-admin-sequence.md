# H5 app factory frontend-before-admin sequence

User correction: H5 frontend and unified-admin backend must not be designed in the same prototype batch by default.

Correct sequence for new H5 projects under the unified backend:

1. inspect source/reference materials;
2. analyze and decompose the H5 core experience;
3. ask blocking questions for H5 user experience, content, payment/member, and data boundaries;
4. build the 750px H5 HTML prototype;
5. wait for user confirmation of the H5 page/function direction;
6. derive backend/admin jobs from the confirmed H5 behavior;
7. ask backend-specific blocking questions for operator workflow, data ownership, payment/order handling, permissions, metrics, and audit;
8. build the unified-admin HTML prototype;
9. wait for user confirmation of backend/admin page/function direction;
10. write the PRD against both confirmed prototypes.

Applied changes:

- Updated `%USERPROFILE%\.codex\skills\app-factory-h5-admin\SKILL.md`.
- Updated `%USERPROFILE%\.codex\skills\app-factory-h5-admin\agents\openai.yaml`.
- Synced the modified app-factory skill into `%USERPROFILE%\Documents\Codex\exports\codex-evolution-export-20260518-165156\skills`.
