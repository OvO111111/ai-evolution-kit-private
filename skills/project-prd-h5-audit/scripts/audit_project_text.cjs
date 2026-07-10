#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const inputs = process.argv.slice(2);
if (!inputs.length) {
  console.error("Usage: node audit_project_text.cjs <file-or-dir> [...]");
  process.exit(2);
}

const checks = [
  ["prd", [/PRD/i, /产品需求/]],
  ["html", [/HTML/i, /原型/]],
  ["membership", [/会员/]],
  ["price_package", [/套餐/, /价格/, /49\.9/, /39\.9/, /59\.9/, /30天/, /30 天/]],
  ["payment_signing", [/支付/, /签约/, /微信支付/, /委托代扣/]],
  ["orders", [/订单/]],
  ["subscription", [/订阅/, /自动续费/, /连续订阅/]],
  ["agreements", [/用户协议/, /用户服务协议/, /隐私政策/, /会员服务协议/, /自动续费/]],
  ["customer_service", [/客服/, /服务电话/, /投诉电话/, /在线客服/]],
  ["legal_subject", [/运营主体/, /企业名称/, /公司主体/, /法律主体/, /服务主体/]],
  ["merchant_short_name", [/商户简称/, /商户短名/, /merchantShortName/i]],
  ["merchant_display", [/商户展示/, /商户名称/, /商户显示/, /merchantDisplayName/i]],
  ["refund", [/退款/]],
  ["aux_rights", [/附属权益/, /主动领取/]],
  ["review_materials", [/审核材料/, /申请材料/, /价目表/, /产品介绍/, /流程图/]],
  ["dev_package", [/开发包/, /交付包/, /\.zip/, /API 契约/, /运行规则/, /asset_manifest/i, /source_images/i]],
  ["archive_wrapper_risk", [/同步时间/, /同步结论/, /归档信息/, /已附截图/, /已附文件/, /本次源文件最新时间/, /bytes/]],
  ["pending_question", [/待确认/, /NEEDS CLARIFICATION/i, /TBD/]],
  ["low_density_prd_risk", [/产品定位/, /用户价值/, /产品目标/, /背景/, /愿景/, /原则/]],
  ["out_of_scope_risk", [/本期不包含/, /不包含/, /非目标/, /暂不支持/, /不做/]],
  ["html_requirement_copy_risk", [/固定四档价格/, /两项核心差异/, /只放短笔记/, /不在信息流中主动打断阅读/, /聚合缓存/, /本地缓存兜底/, /来源字段/, /运营策略/, /低维护/]],
];

function shouldSkip(name) {
  return (
    name === "rule-extraction-summary.md" ||
    name === "index.json" ||
    /^skill-script-.*\.json$/i.test(name)
  );
}

function collect(input) {
  const stat = fs.statSync(input);
  if (stat.isFile()) return shouldSkip(path.basename(input)) ? [] : [input];
  const out = [];
  for (const entry of fs.readdirSync(input, { withFileTypes: true })) {
    if (shouldSkip(entry.name)) continue;
    const file = path.join(input, entry.name);
    if (entry.isDirectory()) out.push(...collect(file));
    else if (/\.(md|txt|html|json|csv)$/i.test(entry.name)) out.push(file);
  }
  return out;
}

function hasAny(text, patterns) {
  return patterns.some((pattern) => pattern.test(text));
}

function classify(name, text) {
  if (/退款/.test(name) || /退款 H5/.test(text)) return "refund_h5";
  if (/内部工具|管理平台|admin|backend/i.test(name)) return "platform_or_admin";
  if (/会员|自动续费|套餐|49\.9|39\.9|59\.9/.test(text)) return "paid_h5";
  return "unknown_or_plain_h5";
}

const files = inputs.flatMap((input) => collect(path.resolve(input)));
const rows = [];

for (const file of files) {
  const text = fs.readFileSync(file, "utf8");
  const row = { file, type: classify(path.basename(file), text) };
  for (const [name, patterns] of checks) row[name] = hasAny(text, patterns);
  rows.push(row);
}

console.log(JSON.stringify({ files: rows.length, rows }, null, 2));
