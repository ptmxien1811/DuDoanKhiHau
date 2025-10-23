// static/js/main.js
document.addEventListener('DOMContentLoaded', () => {
  const cardsRow = document.getElementById('cardsRow');
  const searchInput = document.getElementById('searchInput');
  const btnSearch = document.getElementById('btnSearch');
  const filterLocation = document.getElementById('filterLocation');
  const minPmInput = document.getElementById('minPm');
  const btnFilter = document.getElementById('btnFilter');
  const countResult = document.getElementById('countResult');
  const imageModal = new bootstrap.Modal(document.getElementById('imageModal'));
  const modalImg = document.getElementById('modalImg');

  let sensors = []; // dữ liệu từ server
  let filtered = [];

  // debounce helper
  function debounce(fn, delay=300){
    let t;
    return (...args)=>{ clearTimeout(t); t = setTimeout(()=>fn(...args), delay); };
  }

  // fetch dữ liệu sensor từ backend
  async function loadSensors(){
    try {
      const res = await fetch('/api/sensors');
      if(!res.ok) throw new Error('Lấy dữ liệu lỗi');
      sensors = await res.json();
      applyFilters();
    } catch(err){
      console.error(err);
      cardsRow.innerHTML = `<div class="col-12"><div class="alert alert-danger">Không thể tải dữ liệu cảm biến.</div></div>`;
    }
  }

  // render danh sách cards
  function renderList(list){
    cardsRow.innerHTML = '';
    if(list.length === 0){
      cardsRow.innerHTML = `<div class="col-12"><div class="alert alert-secondary">Không có kết quả</div></div>`;
      countResult.textContent = 0;
      return;
    }
    countResult.textContent = list.length;
    const html = list.map(s => {
      // badge màu theo pm
      let badge = 'badge bg-success';
      if(s.pm25 >= 50 && s.pm25 < 100) badge = 'badge bg-warning text-dark';
      if(s.pm25 >= 100) badge = 'badge bg-danger';

      const imgUrl = s.image ? `/static/img/${s.image}` : '/static/img/sensor-placeholder.jpg';
      return `
      <div class="col-md-4">
        <div class="card h-100 shadow-sm">
          <img src="${imgUrl}" class="card-img-top" alt="${s.name}" loading="lazy" style="cursor:pointer;" data-img="${imgUrl}">
          <div class="card-body d-flex flex-column">
            <h5 class="card-title">${s.name} <span class="${badge} ms-2">${s.pm25}</span></h5>
            <p class="card-text mb-2">Vị trí: <strong>${s.location}</strong></p>
            <p class="card-text text-muted mb-3 small">Cập nhật: ${s.timestamp}</p>
            <div class="mt-auto">
              <a href="javascript:void(0)" class="btn btn-sm btn-outline-primary me-2" data-id="${s.id}" onclick="showDetails('${s.id}')">Xem chi tiết</a>
              <button class="btn btn-sm btn-outline-secondary" onclick="openImage('${imgUrl}')">Xem ảnh</button>
            </div>
          </div>
        </div>
      </div>
      `;
    }).join('');
    cardsRow.innerHTML = html;

    // add click listeners cho img mở modal
    document.querySelectorAll('.card-img-top').forEach(img => {
      img.addEventListener('click', e => {
        const src = e.currentTarget.dataset.img || e.currentTarget.src;
        openImage(src);
      });
    });
  }

  // open image modal
  window.openImage = function(src){
    modalImg.src = src;
    imageModal.show();
  };

  // placeholder function xem chi tiết (có thể mở modal khác hoặc route)
  window.showDetails = function(id){
    const s = sensors.find(x=>String(x.id) === String(id));
    if(!s) return alert('Không tìm thấy sensor');
    alert(`Chi tiết ${s.name}\nPM2.5: ${s.pm25}\nTiếng ồn: ${s.noise}\nVị trí: ${s.location}`);
  };

  // apply filters and search
  function applyFilters(){
    const q = searchInput.value.trim().toLowerCase();
    const loc = filterLocation.value;
    const minPm = parseFloat(minPmInput.value) || 0;

    filtered = sensors.filter(s => {
      const matchQ = q === '' || (
        (s.name && s.name.toLowerCase().includes(q)) ||
        (s.location && s.location.toLowerCase().includes(q))
      );
      const matchLoc = !loc || s.location === loc;
      const matchPm = (s.pm25 || 0) >= minPm;
      return matchQ && matchLoc && matchPm;
    });

    renderList(filtered);
  }

  // events
  btnSearch.addEventListener('click', applyFilters);
  filterLocation.addEventListener('change', applyFilters);
  btnFilter.addEventListener('click', applyFilters);
  searchInput.addEventListener('input', debounce(applyFilters, 300));
  minPmInput.addEventListener('input', debounce(applyFilters, 300));

  // load lúc đầu
  loadSensors();
});
