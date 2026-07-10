const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

function readJson(file) {
  return JSON.parse(fs.readFileSync(file, "utf8").replace(/^\uFEFF/, ""));
}

function fileUrl(filePath) {
  return `file:///${path.resolve(filePath).replace(/\\/g, "/")}`;
}

function esc(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function rel(fromDir, filePath) {
  return path.relative(fromDir, filePath).replace(/\\/g, "/");
}

function renderHtml(config) {
  const accent = config.theme?.accent || "#20D685";
  const glow = config.theme?.glow || "rgba(32, 214, 133, 0.22)";
  const outputDir = path.dirname(path.resolve(config.outputHtml));
  const steps = config.steps.map((step, index) => `
    <article class="step-card">
      <div class="step-num">${index + 1}</div>
      <img class="phone-shot" src="${rel(outputDir, step.assetPath)}" alt="${esc(step.title)}">
      <h2>${esc(step.title)}</h2>
      <p>${esc(step.description)}</p>
    </article>`).join("\n");

  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1600, initial-scale=1.0">
<title>${esc(config.title)}</title>
<style>
*{box-sizing:border-box}html,body{margin:0;padding:0;background:#171B2D}body{width:1600px;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",Arial,sans-serif}.poster{position:relative;width:1600px;height:2220px;overflow:hidden;color:#fff;background:radial-gradient(circle at 50% 6%,${glow},transparent 230px),linear-gradient(180deg,#181D31 0%,#151929 100%)}.title{position:absolute;top:30px;left:0;width:100%;text-align:center;font-size:52px;line-height:1.1;font-weight:950}.subtitle{position:absolute;top:92px;left:0;width:100%;text-align:center;color:#8E96AD;font-size:21px;line-height:1.35;font-weight:650}.section-pill{position:absolute;left:30px;z-index:4;height:30px;padding:0 18px;display:flex;align-items:center;border-radius:999px;background:${accent};color:#fff;font-size:19px;font-weight:900;box-shadow:0 8px 18px rgba(0,0,0,.18)}.section-pill.s1{top:120px}.section-pill.s2{top:840px}.section-pill.s3{top:1558px}.flow-grid{position:absolute;left:88px;top:166px;z-index:3;display:grid;grid-template-columns:repeat(5,270px);column-gap:40px;row-gap:86px}.step-card{position:relative;width:270px;min-height:610px;text-align:center}.step-num{position:absolute;top:-43px;left:50%;transform:translateX(-50%);z-index:5;min-width:52px;height:36px;padding:0 12px;border-radius:999px;display:flex;align-items:center;justify-content:center;background:${accent};color:#fff;font-size:25px;line-height:1;font-weight:950;box-shadow:0 7px 18px rgba(0,0,0,.2)}.phone-shot{width:220px;height:476px;object-fit:contain;display:block;margin:0 auto;filter:drop-shadow(0 12px 20px rgba(0,0,0,.28))}.step-card h2{margin:26px 0 6px;color:#fff;font-size:29px;line-height:1.12;font-weight:950}.step-card p{margin:0 auto;max-width:255px;color:#B7BED1;font-size:17px;line-height:1.35;font-weight:600}.connections{position:absolute;inset:0;z-index:2;pointer-events:none}.arrow{fill:none;stroke:#FF3E5D;stroke-width:4;stroke-linecap:round;stroke-linejoin:round}
</style>
</head>
<body>
<main class="poster">
  <div class="title">${esc(config.title)}</div>
  <div class="subtitle">${esc(config.subtitle || "")}</div>
  <div class="section-pill s1">${esc(config.sections?.[0] || "第一部分：登录与内容使用")}</div>
  <div class="section-pill s2">${esc(config.sections?.[1] || "第二部分：会员开通与支付签约")}</div>
  <div class="section-pill s3">${esc(config.sections?.[2] || "第三部分：退订、客服与协议查看")}</div>
  <svg class="connections" width="1600" height="2220" viewBox="0 0 1600 2220">
    <defs><marker id="arrowHead" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L10,5 L0,10 Z" fill="#FF3E5D"></path></marker></defs>
    <path class="arrow" marker-end="url(#arrowHead)" d="M342 400 H387"></path><path class="arrow" marker-end="url(#arrowHead)" d="M652 400 H697"></path><path class="arrow" marker-end="url(#arrowHead)" d="M962 400 H1007"></path><path class="arrow" marker-end="url(#arrowHead)" d="M1272 400 H1317"></path>
    <path class="arrow" d="M1368 760 V800 H232 V838"></path><path class="arrow" marker-end="url(#arrowHead)" d="M232 838 v18"></path>
    <path class="arrow" marker-end="url(#arrowHead)" d="M342 1120 H387"></path><path class="arrow" marker-end="url(#arrowHead)" d="M652 1120 H697"></path><path class="arrow" marker-end="url(#arrowHead)" d="M962 1120 H1007"></path><path class="arrow" marker-end="url(#arrowHead)" d="M1272 1120 H1317"></path>
    <path class="arrow" d="M1368 1480 V1518 H232 V1556"></path><path class="arrow" marker-end="url(#arrowHead)" d="M232 1556 v18"></path>
    <path class="arrow" marker-end="url(#arrowHead)" d="M342 1840 H387"></path><path class="arrow" marker-end="url(#arrowHead)" d="M652 1840 H697"></path><path class="arrow" marker-end="url(#arrowHead)" d="M962 1840 H1007"></path><path class="arrow" marker-end="url(#arrowHead)" d="M1272 1840 H1317"></path>
  </svg>
  <section class="flow-grid">${steps}</section>
</main>
</body>
</html>`;
}

async function main() {
  const configPath = process.argv[2];
  if (!configPath) {
    throw new Error("Usage: node render-h5-flowchart.js <config.json>");
  }
  const config = readJson(configPath);
  if (!config.sourceHtml || !config.outputHtml || !config.outputPng || !Array.isArray(config.steps)) {
    throw new Error("Config must include sourceHtml, outputHtml, outputPng, and steps.");
  }

  const outputDir = path.dirname(path.resolve(config.outputHtml));
  const assetDir = path.resolve(config.assetDir || path.join(outputDir, "flow-assets"));
  fs.mkdirSync(assetDir, { recursive: true });
  fs.mkdirSync(outputDir, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  try {
    const sourcePage = await browser.newPage({ viewport: { width: 1440, height: 2200 }, deviceScaleFactor: 1 });
    await sourcePage.goto(fileUrl(config.sourceHtml), { waitUntil: "load" });
    const frames = await sourcePage.$$(config.frameSelector || ".phone-frame");
    if (!frames.length) {
      throw new Error(`No frames found with selector ${config.frameSelector || ".phone-frame"}`);
    }

    for (let i = 0; i < config.steps.length; i += 1) {
      const step = config.steps[i];
      const frame = frames[step.frameIndex];
      if (!frame) {
        throw new Error(`Missing frame index ${step.frameIndex} for step ${i + 1}`);
      }
      step.assetPath = path.join(assetDir, `${String(i + 1).padStart(2, "0")}.png`);
      await frame.screenshot({ path: step.assetPath, animations: "disabled" });
    }
    await sourcePage.close();

    fs.writeFileSync(config.outputHtml, renderHtml(config), "utf8");
    const posterPage = await browser.newPage({ viewport: { width: 1600, height: 2220 }, deviceScaleFactor: 1 });
    await posterPage.goto(fileUrl(config.outputHtml), { waitUntil: "load" });
    await posterPage.screenshot({ path: config.outputPng, fullPage: true, animations: "disabled" });
    await posterPage.close();
    console.log(`${config.outputPng} rendered`);
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
