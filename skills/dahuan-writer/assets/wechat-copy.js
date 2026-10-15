// 普通公众号图文的正文复制逻辑；接入要求见 references/publication.md。
(function () {
  const button = document.getElementById('copy-wechat');
  const message = document.getElementById('copy-message');
  const article = document.querySelector('article');

  function makeCopy() {
    const copy = article.cloneNode(true);
    copy.querySelectorAll('h1, .status').forEach(el => el.remove());
    const text = Array.from(copy.children).map(el => el.textContent.trim()).filter(Boolean).join('\n\n');
    const originalImages = Array.from(article.querySelectorAll('img'));
    copy.querySelectorAll('p').forEach(el => {
      const caption = el.classList.contains('caption');
      el.setAttribute('style', caption
        ? 'text-align:left;font-size:13px;line-height:1.7;margin:0 0 24px;color:#888888;'
        : 'text-align:left;font-size:17px;line-height:1.8;margin:0 0 24px;color:#333333;');
    });
    copy.querySelectorAll('strong,b').forEach(el => {
      const color = el.style.color || '#333333';
      el.setAttribute('style', 'text-align:left;font-weight:700;color:' + color + ';');
    });
    copy.querySelectorAll('a').forEach(el => {
      el.setAttribute('style', 'text-align:left;color:#4c6d83;text-decoration:underline;');
    });
    copy.querySelectorAll('img').forEach((img, index) => {
      const original = originalImages[index];
      img.src = original.src;
      img.removeAttribute('width');
      img.removeAttribute('height');
      img.setAttribute('style', 'display:block;width:100%;max-width:100%;height:auto;margin:0;border:0;');
      if (original.naturalWidth) {
        img.setAttribute('data-w', String(original.naturalWidth));
        img.setAttribute('data-ratio', String(original.naturalHeight / original.naturalWidth));
      }
    });
    copy.querySelectorAll('figure,blockquote').forEach(el => {
      const section = document.createElement('section');
      section.setAttribute('style', el.tagName === 'BLOCKQUOTE'
        ? 'text-align:left;margin:0 0 24px;padding:16px;box-sizing:border-box;border-left:3px solid #bdc9c6;background-color:#f5f7f6;'
        : 'text-align:left;margin:0 0 12px;padding:0;');
      while (el.firstChild) section.appendChild(el.firstChild);
      el.replaceWith(section);
    });
    copy.querySelectorAll('[class]').forEach(el => el.removeAttribute('class'));
    const section = document.createElement('section');
    section.setAttribute('style', 'text-align:left;font-size:17px;line-height:1.8;color:#333333;margin:0;padding:0;');
    while (copy.firstChild) section.appendChild(copy.firstChild);
    return {html: section.outerHTML, text};
  }

  button.addEventListener('click', async function () {
    const content = makeCopy();
    if (navigator.clipboard && navigator.clipboard.write && window.ClipboardItem) {
      try {
        await navigator.clipboard.write([new ClipboardItem({
          'text/html': new Blob([content.html], {type: 'text/html'}),
          'text/plain': new Blob([content.text], {type: 'text/plain'})
        })]);
        message.textContent = '已复制正文，回到公众号粘贴即可。';
      } catch (error) {
        message.textContent = '复制未完成，请允许浏览器复制后再试。';
      }
      return;
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
    message.textContent = success && wrote
      ? '已复制正文，回到公众号粘贴即可。'
      : '复制未完成，请选中正文后手动复制。';
  });
})();
