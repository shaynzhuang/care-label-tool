(function () {
  const BASE = '/care-label-generator';
  if (!location.pathname.startsWith(BASE)) return;

  const isZh = () => document.documentElement.lang.toLowerCase().startsWith('zh');
  const words = {
    button: ['从 tracker 选择', 'Choose from tracker'],
    title: ['从 tracker 选择款式', 'Choose styles from tracker'],
    hint: ['选择生产单可带入实际订单资料；样衣用于尚未开生产单的款。', 'Choose an order for actual production data, or a sample without a production order.'],
    orders: ['生产单', 'Production orders'], samples: ['样衣', 'Samples'],
    search: ['款号、款名、客户或单号', 'Style, customer, or order number'],
    searchButton: ['搜索', 'Search'], close: ['关闭', 'Close'],
    selectPage: ['全选当前结果', 'Select all results'],
    empty: ['输入关键词搜索，或查看最近资料。', 'Search by keyword or browse recent records.'],
    none: ['没有匹配的记录。', 'No matching records.'],
    loading: ['正在读取 tracker…', 'Loading tracker data…'],
    error: ['读取失败，请刷新后重试。', 'Could not load data. Please refresh and try again.'],
    chosen: ['已选', 'Selected'],
    loadOne: ['载入所选款式', 'Load selected style'],
    loadMany: ['生成所选款式', 'Generate selected styles'],
    printQty: ['把来源数量印在标签上（默认只用于核对）', 'Print source quantity on labels (off by default)'],
    missingComp: ['缺英文成分，载入后需补充', 'English composition missing; fill it in after loading'],
    noQty: ['数量未录', 'Quantity not recorded'],
    sourceOrder: ['生产单', 'Order'], sourceSample: ['样衣', 'Sample'],
    loaded: ['已载入', 'Loaded'],
    qtyRef: ['来源数量', 'Source quantity'],
    notPrinted: ['数量仅用于核对，没有印在标签上。', 'Quantity is for reference and was not printed on the label.'],
    missingEnglish: ['tracker 没有英文面料成分，请补充后再打印。', 'Tracker has no English composition. Add it before printing.'],
    missingBrand: ['品牌无法识别，请核对模板和追踪码。', 'Brand could not be identified. Check the template and tracking code.'],
    missingPrintQty: ['所选记录有未录数量，不能把数量印到标签上。', 'Some selected records have no quantity, so quantity printing is unavailable.'],
    missingSourceQty: ['tracker 未记录来源数量', 'Tracker has no source quantity'],
    generated: ['已载入批量预览。来源数量仅供核对，默认不会印在标签上。', 'Batch preview loaded. Source quantities are for reference and are not printed by default.'],
    currentLabelQty: ['来源数量已填入标签数量栏。', 'Source quantity was placed in the label quantity field.']
  };
  const t = key => words[key][isZh() ? 0 : 1];
  const byId = id => document.getElementById(id);

  const css = document.createElement('style');
  css.textContent = `
    .tracker-pick-dialog{width:min(880px,calc(100vw - 24px));max-height:min(90vh,860px);padding:0;border:1px solid #e5e6eb;border-radius:14px;color:#1f2329;background:#fff;box-shadow:0 24px 80px rgba(17,24,39,.24)}
    .tracker-pick-dialog::backdrop{background:rgba(20,25,35,.48);backdrop-filter:blur(3px)}
    .tracker-pick-head{padding:20px 22px 14px;border-bottom:1px solid #eceef2;display:flex;align-items:flex-start;justify-content:space-between;gap:18px}
    .tracker-pick-head h2{margin:0;font-size:19px;font-weight:650}.tracker-pick-head p{margin:5px 0 0;color:#758091;font-size:12px;line-height:1.5}
    .tracker-pick-close{border:0;background:transparent;font-size:24px;line-height:1;color:#697386;cursor:pointer;padding:0 4px}
    .tracker-pick-controls{padding:14px 22px 10px;display:grid;gap:12px}
    .tracker-pick-tabs{display:flex;gap:7px}.tracker-pick-tab{border:1px solid #d8dce4;background:#fff;color:#576173;border-radius:7px;padding:7px 12px;font:inherit;font-size:13px;cursor:pointer}
    .tracker-pick-tab.active{background:#165dff;border-color:#165dff;color:#fff}
    .tracker-pick-search{display:flex;gap:8px}.tracker-pick-search input{flex:1;min-width:0;padding:10px 12px;border:1px solid #d8dce4;border-radius:7px;font:inherit;font-size:14px}
    .tracker-pick-search button,.tracker-pick-select-all,.tracker-pick-footer button{border:1px solid #d8dce4;border-radius:7px;background:#fff;padding:8px 12px;font:inherit;font-size:13px;cursor:pointer;color:#344054}
    .tracker-pick-search button.primary,.tracker-pick-footer button.primary{background:#165dff;color:#fff;border-color:#165dff}
    .tracker-pick-count{padding:0 22px 9px;display:flex;justify-content:space-between;align-items:center;color:#687386;font-size:12px}
    .tracker-pick-results{padding:0 22px 12px;overflow:auto;max-height:48vh;min-height:150px}
    .tracker-pick-card{display:grid;grid-template-columns:22px 52px minmax(0,1fr) auto;gap:11px;align-items:center;padding:11px 2px;border-top:1px solid #eef0f3;cursor:pointer}
    .tracker-pick-card input{width:16px;height:16px}.tracker-pick-thumb{width:52px;height:52px;object-fit:cover;border-radius:7px;background:#f0f2f5}
    .tracker-pick-placeholder{width:52px;height:52px;border-radius:7px;background:#f0f2f5;display:grid;place-items:center;color:#7b8492;font-size:11px}
    .tracker-pick-main{min-width:0}.tracker-pick-primary{display:flex;gap:8px;align-items:center;flex-wrap:wrap;font-size:13px;font-weight:650;color:#202633}
    .tracker-pick-secondary{margin-top:3px;color:#687386;font-size:12px;overflow-wrap:anywhere}.tracker-pick-composition{margin-top:3px;color:#87909e;font-size:11px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
    .tracker-pick-qty{white-space:nowrap;font-size:12px;color:#475467;background:#f4f6f8;border-radius:6px;padding:5px 8px}
    .tracker-pick-missing{font-weight:500;color:#b54708;background:#fff4e5;border-radius:5px;padding:2px 6px;font-size:10px}
    .tracker-pick-empty{padding:38px 10px;text-align:center;color:#7c8797;font-size:13px}
    .tracker-pick-toast{position:fixed;z-index:1000;right:22px;bottom:22px;max-width:min(440px,calc(100vw - 32px));padding:12px 16px;border-radius:9px;background:#253047;color:#fff;box-shadow:0 10px 32px rgba(17,24,39,.22);font-size:13px;line-height:1.45;white-space:pre-line}
    .tracker-pick-toast.warning{background:#7a3216}
    .tracker-pick-footer{padding:12px 22px 18px;border-top:1px solid #eceef2;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
    .tracker-pick-footer label{display:flex;align-items:center;gap:7px;font-size:12px;color:#596579;line-height:1.4}.tracker-pick-footer input{width:15px;height:15px}
    .tracker-pick-actions{display:flex;gap:8px}
    @media(max-width:600px){.tracker-pick-head,.tracker-pick-controls,.tracker-pick-footer{padding-left:14px;padding-right:14px}.tracker-pick-count,.tracker-pick-results{padding-left:14px;padding-right:14px}.tracker-pick-results{max-height:55vh}.tracker-pick-card{grid-template-columns:20px 42px minmax(0,1fr);gap:8px}.tracker-pick-thumb,.tracker-pick-placeholder{width:42px;height:42px}.tracker-pick-qty{grid-column:3;justify-self:start;margin-top:-3px}.tracker-pick-search{flex-wrap:wrap}.tracker-pick-search input{flex-basis:100%}.tracker-pick-footer{align-items:flex-start}.tracker-pick-actions{width:100%;justify-content:flex-end}}
  `;
  document.head.appendChild(css);

  const topActions = document.querySelector('.topbar > div:last-child');
  if (!topActions || typeof render !== 'function') return;

  const openButton = document.createElement('button');
  openButton.type = 'button';
  openButton.className = 'btn ghost';
  openButton.textContent = t('button');
  topActions.prepend(openButton);

  const dialog = document.createElement('dialog');
  dialog.className = 'tracker-pick-dialog';
  dialog.innerHTML = `
    <div class="tracker-pick-head"><div><h2>${t('title')}</h2><p>${t('hint')}</p></div><button class="tracker-pick-close" type="button" aria-label="${t('close')}">×</button></div>
    <div class="tracker-pick-controls">
      <div class="tracker-pick-tabs"><button class="tracker-pick-tab active" type="button" data-source="orders">${t('orders')}</button><button class="tracker-pick-tab" type="button" data-source="samples">${t('samples')}</button></div>
      <div class="tracker-pick-search"><input id="trackerPickQuery" type="search" placeholder="${t('search')}"><button class="primary" type="button" id="trackerPickSearch">${t('searchButton')}</button></div>
    </div>
    <div class="tracker-pick-count"><span id="trackerPickCount">${t('empty')}</span><button class="tracker-pick-select-all" type="button" id="trackerPickSelectAll">${t('selectPage')}</button></div>
    <div class="tracker-pick-results" id="trackerPickResults" aria-live="polite"></div>
    <div class="tracker-pick-footer"><label><input id="trackerPickPrintQty" type="checkbox">${t('printQty')}</label><div class="tracker-pick-actions"><button type="button" id="trackerPickCancel">${t('close')}</button><button type="button" class="primary" id="trackerPickLoad" disabled>${t('loadOne')}</button></div></div>
  `;
  document.body.appendChild(dialog);

  let sourceType = 'orders';
  let records = [];
  const selected = new Map();
  let requestController = null;
  let debounceTimer = null;
  const queryInput = byId('trackerPickQuery');
  const results = byId('trackerPickResults');
  const count = byId('trackerPickCount');
  const loadButton = byId('trackerPickLoad');
  const printQuantity = byId('trackerPickPrintQty');

  function keyOf(record) { return sourceType + ':' + record.id; }
  function updateSelection() {
    count.textContent = t('chosen') + ' ' + selected.size;
    loadButton.disabled = selected.size === 0;
    loadButton.textContent = selected.size > 1 ? t('loadMany') : t('loadOne');
  }
  function displayQuantity(record) {
    return record.quantity == null ? t('noQty') : Number(record.quantity).toLocaleString(isZh() ? 'zh-CN' : 'en-US');
  }
  function notify(message, warning) {
    const toast = document.createElement('div');
    toast.className = 'tracker-pick-toast' + (warning ? ' warning' : '');
    toast.setAttribute('role', warning ? 'alert' : 'status');
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 5200);
  }
  function createRecordCard(record) {
    const card = document.createElement('label');
    card.className = 'tracker-pick-card';
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = selected.has(keyOf(record));
    checkbox.addEventListener('change', () => {
      if (checkbox.checked) selected.set(keyOf(record), record);
      else selected.delete(keyOf(record));
      updateSelection();
    });

    let image;
    if (record.imageUrl && /^\/uploads\/samples\/[\w\-.%()\u4e00-\u9fff]+$/i.test(record.imageUrl)) {
      image = document.createElement('img');
      image.className = 'tracker-pick-thumb';
      image.src = record.imageUrl;
      image.alt = '';
      image.loading = 'lazy';
    } else {
      image = document.createElement('div');
      image.className = 'tracker-pick-placeholder';
      image.textContent = record.styleNo ? record.styleNo.slice(0, 3) : '—';
    }

    const main = document.createElement('div');
    main.className = 'tracker-pick-main';
    const primary = document.createElement('div');
    primary.className = 'tracker-pick-primary';
    const ref = document.createElement('span');
    ref.textContent = record.orderNo || record.sampleNo || '';
    const style = document.createElement('span');
    style.textContent = record.styleNo || (isZh() ? '款号未填写' : 'No style number');
    primary.append(ref, style);
    if (!record.compositionEn) {
      const missing = document.createElement('span');
      missing.className = 'tracker-pick-missing';
      missing.textContent = t('missingComp');
      primary.appendChild(missing);
    }
    const secondary = document.createElement('div');
    secondary.className = 'tracker-pick-secondary';
    secondary.textContent = [record.customer, record.styleName, record.brandName].filter(Boolean).join(' · ') || '—';
    const comp = document.createElement('div');
    comp.className = 'tracker-pick-composition';
    const compSource = record.compositionSource === 'sample-current'
      ? (isZh() ? ' · 成分取样衣当前资料，请核对' : ' · current sample composition; please verify') : '';
    comp.textContent = (record.compositionEn || record.compositionZh || (isZh() ? '未填写面料成分' : 'Composition not entered')) + compSource;
    main.append(primary, secondary, comp);

    const qty = document.createElement('span');
    qty.className = 'tracker-pick-qty';
    qty.textContent = displayQuantity(record) + (record.sourceType === 'sample' ? (isZh() ? ' 件（样衣）' : ' pcs · sample') : (isZh() ? ' 件' : ' pcs'));
    card.append(checkbox, image, main, qty);
    return card;
  }
  function renderRecords() {
    results.replaceChildren();
    if (!records.length) {
      const empty = document.createElement('div');
      empty.className = 'tracker-pick-empty';
      empty.textContent = t('none');
      results.appendChild(empty);
    } else {
      records.forEach(record => results.appendChild(createRecordCard(record)));
    }
    count.textContent = (isZh() ? '找到 ' : 'Found ') + records.length + (isZh() ? ' 条' : ' records');
    updateSelection();
  }
  async function search() {
    if (requestController) requestController.abort();
    requestController = new AbortController();
    results.replaceChildren();
    const loading = document.createElement('div');
    loading.className = 'tracker-pick-empty';
    loading.textContent = t('loading');
    results.appendChild(loading);
    try {
      const params = new URLSearchParams({ type: sourceType, q: queryInput.value.trim() });
      const response = await fetch(BASE + '/data?' + params.toString(), {
        credentials: 'same-origin', headers: { Accept: 'application/json' }, signal: requestController.signal
      });
      if (!response.ok) throw new Error('HTTP ' + response.status);
      const data = await response.json();
      records = Array.isArray(data.items) ? data.items : [];
      renderRecords();
    } catch (error) {
      if (error.name === 'AbortError') return;
      results.replaceChildren();
      const message = document.createElement('div');
      message.className = 'tracker-pick-empty';
      message.textContent = t('error');
      results.appendChild(message);
      count.textContent = t('error');
    }
  }

  function batchFromTracker(items) {
    const presets = loadPresets();
    const country = +byId('country').value;
    const mergeAll = byId('mergeAll').checked;
    const batchItems = items.map((record, index) => {
      const style = String(record.styleNo || '').trim();
      const comp = String(record.compositionEn || '').trim();
      const brand = brandFromText(record.brandName) || brandCode(style);
      const tpl = (BRANDS[brand] || { tpl: 'a_adv' }).tpl;
      const notes = [];
      if (!BRANDS[brand]) notes.push(isZh() ? '品牌无法识别，请核对模板' : 'Brand could not be identified; check the template');
      if (!comp) notes.push(isZh() ? '没有英文面料成分，需要补充' : 'English composition is missing');
      if (record.quantity == null) notes.push(t('missingSourceQty'));
      checkPct(comp).forEach(issue => notes.push((isZh() ? '成分百分比异常：' : 'Composition total is not 100%: ') + issue));
      const sel = Object.assign({}, presets[brand] || PRESET_BUILTIN.S27SH);
      sel.extras = (sel.extras || []).slice();
      if (tpl === 'c') {
        const missing = translateComp(comp, 1).missing;
        if (missing.length) notes.push((isZh() ? '缺法语/西语译名：' : 'Missing FR/ES translation: ') + [...new Set(missing)].join(', '));
        const missingCare = missingFrEs(careOf(sel));
        if (missingCare.length) notes.push((isZh() ? '洗护规则缺法语/西语：' : 'Care rule missing FR/ES: ') + missingCare.join(', '));
      }
      return { row: index + 1, style, comp, qty: Number(record.quantity) || 0, gender: '', brand, tpl, sel, country, notes };
    });

    const groups = [];
    const groupMap = new Map();
    batchItems.forEach(item => {
      const key = [item.brand, item.gender, normCompKey(item.comp), JSON.stringify(item.sel), item.country, (item.tpl !== 'c' && !mergeAll) ? item.style : ''].join('|');
      let group = groupMap.get(key);
      if (!group) {
        group = { brand: item.brand, tpl: item.tpl, gender: item.gender, comp: item.comp, sel: item.sel, country: item.country, items: [], notes: [] };
        groupMap.set(key, group);
        groups.push(group);
      }
      group.items.push(item);
      item.notes.forEach(note => { if (!group.notes.includes(note)) group.notes.push(note); });
    });
    const brandOrder = Object.keys(BRANDS);
    groups.sort((a, b) => (brandOrder.indexOf(a.brand) + 100 * (brandOrder.indexOf(a.brand) < 0)) - (brandOrder.indexOf(b.brand) + 100 * (brandOrder.indexOf(b.brand) < 0)) || a.gender.localeCompare(b.gender));
    groups.forEach((group, index) => {
      group.no = index + 1;
      group.total = group.items.reduce((sum, item) => sum + item.qty, 0);
      group.styles = [...new Set(group.items.map(item => item.style))];
      group.qtys = group.items.map(item => item.qty);
      group.track = trackCode(group.brand);
    });
    const sourceLabel = sourceType === 'orders' ? 'orders' : 'samples';
    BATCH = { groups, items: batchItems, file: 'tracker-' + sourceLabel, qtyHeader: isZh() ? '来源数量（只供核对）' : 'Source quantity (reference only)', hideLabelQuantity: !printQuantity.checked };
    renderBatch();
  }

  function loadSelected() {
    const chosen = [...selected.values()];
    if (!chosen.length) return;
    if (printQuantity.checked && chosen.some(record => record.quantity == null)) {
      count.textContent = t('missingPrintQty');
      return;
    }
    dialog.close();
    if (chosen.length === 1) {
      if (BATCH) exitBatch();
      const record = chosen[0];
      byId('styleNo').value = record.styleNo || '';
      byId('composition').value = record.compositionEn || '';
      byId('brandOverride').value = brandFromText(record.brandName) || '';
      byId('templateOverride').value = 'auto';
      byId('trackOverride').value = '';
      byId('qty').value = printQuantity.checked && record.quantity != null ? String(record.quantity) : '';
      render();
      const message = [t('loaded') + ' ' + (record.orderNo || record.sampleNo || record.styleNo), displayQuantity(record) + ' ' + t('qtyRef'), printQuantity.checked ? t('currentLabelQty') : t('notPrinted')];
      if (!record.compositionEn) message.push(t('missingEnglish'));
      if (!brandFromText(record.brandName) && !BRANDS[brandCode(record.styleNo || '')]) message.push(t('missingBrand'));
      notify(message.join('\n'), !record.compositionEn || (!brandFromText(record.brandName) && !BRANDS[brandCode(record.styleNo || '')]));
    } else {
      if (BATCH) exitBatch();
      batchFromTracker(chosen);
      notify(t('generated'));
    }
    selected.clear();
    updateSelection();
  }

  openButton.addEventListener('click', () => {
    selected.clear();
    updateSelection();
    queryInput.value = '';
    printQuantity.checked = false;
    dialog.showModal();
    search();
    setTimeout(() => queryInput.focus(), 0);
  });
  dialog.querySelector('.tracker-pick-close').addEventListener('click', () => dialog.close());
  byId('trackerPickCancel').addEventListener('click', () => dialog.close());
  byId('trackerPickSearch').addEventListener('click', search);
  queryInput.addEventListener('keydown', event => { if (event.key === 'Enter') { event.preventDefault(); search(); } });
  queryInput.addEventListener('input', () => { clearTimeout(debounceTimer); debounceTimer = setTimeout(search, 280); });
  dialog.querySelectorAll('.tracker-pick-tab').forEach(tab => tab.addEventListener('click', () => {
    sourceType = tab.dataset.source;
    selected.clear();
    dialog.querySelectorAll('.tracker-pick-tab').forEach(button => button.classList.toggle('active', button === tab));
    updateSelection();
    search();
  }));
  byId('trackerPickSelectAll').addEventListener('click', () => {
    records.forEach(record => selected.set(keyOf(record), record));
    renderRecords();
  });
  loadButton.addEventListener('click', loadSelected);
})();
