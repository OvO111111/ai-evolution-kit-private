# Reusable Module Map

## New Project Intake

Capture these fields before production:

- `app_id`: stable lowercase identifier
- `app_name`: display name
- `one_sentence_job`: what the user accomplishes
- `content_modality`: image/text, video, article, checklist, product card, audio, or mixed
- `primary_content_unit`: the object managed by frontend and admin
- `taxonomy`: categories, tags, scenes, or filters
- `access_model`: free, VIP, subscription, one-time purchase, or no payment
- `publish_model`: manual publish, scheduled publish, weekly issue, or rolling library
- `admin_roles`: super admin, app admin, editor, viewer
- `review_materials`: whether the project needs application/review assets such as process-flow diagrams, product price-list images, product-introduction images, screenshots, agreements, or downloadable attachments

## Module Selection

Always select modules deliberately:

| Module | Include When | Typical Fields |
|---|---|---|
| App registry | every app | app_id, name, icon, status, config |
| Content library | every content app | title, category, tags, status, sort_order, published_at |
| Media assets | image/audio/video apps | cover_url, media_urls, storage paths, dimensions/duration |
| Detail/editor | every content app | summary, body, metadata, preview state |
| Recommendation slots | curated apps | issue_no, featured, ranking, reason |
| Config | every app | price, switches, category dictionary, publish cadence |
| Products | paid apps | product_id, price_cent, duration_days, enabled, purchasable |
| Orders | paid apps | order_id, user_id/openid, amount, status, created_at |
| Users/members | paid or personalized apps | member_status, expire_at, preferences |
| Review material center | paid/subscription or application-reviewed apps | artifact_type, title, brand, version, file_url, source_url, thumbnail_url, owner, status, updated_at |
| Accounts/permissions | unified platform | role, app_ids, status, last_login |

## Paid H5 Review Material Center

Include this module when the H5 project needs WeChat Pay, delegated-deduction review, merchant application evidence, or user-facing review packages.

- Artifact types: process-flow diagram, product price list, product introduction page, H5 screenshot, user agreement, privacy policy, membership service agreement, auto-renewal agreement.
- Admin actions: upload, replace with version note, preview, download, publish/unpublish, assign brand/version.
- PRD requirement: describe this as a standalone module so the user can view and download artifacts directly from the PRD/admin surface instead of searching local folders.
- Brand rule: each branded version has its own artifact group. Do not mix company subjects, customer-service numbers, merchant display names, or legal artifacts.

## Example Mapping: Weekly Outfit

Use the project as an image/text recommendation app:

- Primary content unit: weekly outfit issue.
- H5 pages: latest issue, style/category browse, issue detail, saved looks or mine, upgrade/paywall if paid. Default design width is `750px`.
- Content fields: title, issue_no, cover_image, image_gallery, summary, style_tags, scene_tags, weather_tags, body_shape_tags, item_list, recommendation_reason, is_free, is_published, sort_order, published_at.
- Admin pages: issue list, create/edit drawer, image upload/gallery management, tags/category config, publish status, pricing/products if paid, orders if paid, review material center if application artifacts are required.
- Do not use audio player, duration, background playback, or sleep-specific copy.
- Keep the unified admin shell and app switcher; only replace app-specific nav labels, table columns, form fields, and config dictionaries.
- Do not output Mini Program-specific files or assumptions by default.
