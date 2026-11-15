// 公众号图文预览一键复制与手动 Cmd/Ctrl+C 复制兼容脚本；约定见 references/publication.md。
(function () {
  const button = document.getElementById('copy-wechat');
  const titleButton = document.getElementById('copy-title');
  const message = document.getElementById('copy-message');
  const article = document.querySelector('article');
  if (!article) return;

  function makeCopy() {
    const copy = article.cloneNode(true);
    copy.querySelectorAll('h1, .status, .controls').forEach(el => el.remove());

    // 保留 <svg> 内部元素 id（供 textPath href / animate mpath 使用），仅移除外层节点 id
    copy.querySelectorAll('[id]').forEach(el => {
      if (!el.closest('svg')) el.removeAttribute('id');
    });

    const text = Array.from(copy.children)
      .map(el => el.textContent.trim())
      .filter(Boolean)
      .join('\n\n');

    const originalImages = Array.from(article.querySelectorAll('img'));

    copy.querySelectorAll('h2, h3').forEach(el => {
      if (el.closest('svg')) return;
      const isH2 = el.tagName === 'H2';
      el.setAttribute('style', isH2
        ? 'text-align:left;font-size:20px;font-weight:700;line-height:1.45;margin:32px 0 14px;color:#111111;'
        : 'text-align:left;font-size:17px;font-weight:700;line-height:1.5;margin:24px 0 10px;color:#111111;');
    });

    copy.querySelectorAll('p').forEach(el => {
      if (el.closest('svg')) return;
      const caption = el.classList.contains('caption');
      el.setAttribute('style', caption
        ? 'text-align:center;font-size:13px;line-height:1.7;margin:0 0 24px;color:#888888;'
        : 'text-align:left;font-size:16px;line-height:1.8;margin:0 0 20px;color:#333333;');
    });

    copy.querySelectorAll('ul, ol').forEach(el => {
      if (el.closest('svg')) return;
      el.setAttribute('style', 'text-align:left;font-size:16px;line-height:1.8;margin:0 0 20px;padding-left:22px;color:#333333;');
    });

    copy.querySelectorAll('li').forEach(el => {
      if (el.closest('svg')) return;
      el.setAttribute('style', 'margin:0 0 8px;');
    });

    copy.querySelectorAll('strong, b').forEach(el => {
      if (el.closest('svg')) return;
      const color = el.style.color || '#111111';
      el.setAttribute('style', 'text-align:left;font-weight:700;color:' + color + ';');
    });

    copy.querySelectorAll('code').forEach(el => {
      if (el.closest('svg')) return;
      el.setAttribute('style', 'font-family:Menlo,Monaco,Consolas,monospace;font-size:14px;background-color:#f4f5f7;color:#1f2937;padding:2px 6px;border-radius:4px;');
    });

    copy.querySelectorAll('a').forEach(el => {
      if (el.closest('svg')) return;
      el.setAttribute('style', 'text-align:left;color:#4c6d83;text-decoration:underline;');
    });

    copy.querySelectorAll('img').forEach((img, index) => {
      const original = originalImages[index];
      if (!original) return;
      img.src = original.src;
      img.removeAttribute('width');
      img.removeAttribute('height');
      img.setAttribute('style', 'display:block;width:100%;max-width:100%;height:auto;margin:0;border:0;border-radius:6px;');
      if (original.naturalWidth) {
        img.setAttribute('data-w', String(original.naturalWidth));
        img.setAttribute('data-ratio', String(original.naturalHeight / original.naturalWidth));
      }
    });

    copy.querySelectorAll('figure, blockquote').forEach(el => {
      const section = document.createElement('section');
      section.setAttribute('style', el.tagName === 'BLOCKQUOTE'
        ? 'text-align:left;margin:0 0 24px;padding:16px;box-sizing:border-box;border-left:3px solid #bdc9c6;background-color:#f5f7f6;'
        : 'text-align:left;margin:0 0 12px;padding:0;');
      while (el.firstChild) section.appendChild(el.firstChild);
      el.replaceWith(section);
    });

    copy.querySelectorAll('[class]').forEach(el => {
      if (!el.closest('svg')) el.removeAttribute('class');
    });

    const section = document.createElement('section');
    section.setAttribute('style', 'text-align:left;font-size:16px;line-height:1.8;color:#333333;margin:0;padding:0;');
    while (copy.firstChild) section.appendChild(copy.firstChild);
    return {html: section.outerHTML, text};
  }

  function showMsg(text) {
    if (message) message.textContent = text;
  }

  async function writeClipboard(content) {
    if (navigator.clipboard && navigator.clipboard.write && window.ClipboardItem) {
      try {
        await navigator.clipboard.write([new ClipboardItem({
          'text/html': new Blob([content.html], {type: 'text/html'}),
          'text/plain': new Blob([content.text], {type: 'text/plain'})
        })]);
        showMsg('已复制公众号内联正文，回到公众号编辑器直接粘贴即可。');
        return true;
      } catch (error) {
        // Fallback below
      }
    }
    let wrote = false;
    function onCopy(event) {
      if (!event.clipboardData) return;
      event.clipboardData.setData('text/html', content.html);
      event.clipboardData.setData('text/plain', content.text);
      event.preventDefault();
      wrote = true;
    }
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(article);
    selection.removeAllRanges();
    selection.addRange(range);
    document.addEventListener('copy', onCopy);
    let success = false;
    try { success = document.execCommand('copy'); } catch (error) { success = false; }
    document.removeEventListener('copy', onCopy);
    selection.removeAllRanges();
    showMsg(success && wrote
      ? '已复制公众号内联正文，回到公众号编辑器直接粘贴即可。'
      : '复制未完成，请允许浏览器剪贴板权限或手动复制。');
    return success && wrote;
  }

  if (button) {
    button.addEventListener('click', function () {
      writeClipboard(makeCopy());
    });
  }

  if (titleButton) {
    titleButton.addEventListener('click', async function () {
      const h1 = article.querySelector('h1') || document.getElementById('article-title');
      const titleText = h1 ? h1.textContent.trim() : '';
      if (!titleText) return;
      try {
        await navigator.clipboard.writeText(titleText);
        showMsg('已复制标题：' + titleText);
      } catch (error) {
        showMsg('标题复制失败，请手动复制。');
      }
    });
  }

  // 允许用户在正文区域直接 Ctrl/Cmd+C 时同步输出微信内联 HTML
  document.addEventListener('copy', function (event) {
    const sel = window.getSelection();
    if (!sel || sel.isCollapsed || !event.clipboardData) return;
    if (!article.contains(sel.anchorNode)) return;
    const content = makeCopy();
    event.clipboardData.setData('text/html', content.html);
    event.clipboardData.setData('text/plain', content.text);
    event.preventDefault();
    showMsg('已拦截并复制微信内联格式正文。');
  });
})();
