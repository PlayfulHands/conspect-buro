<template>
  <div class="client-page">
    <header class="client-header">
      <div class="logo" @click="$router.push('/')">← На главную</div>
      <h1>Мои заявки</h1>
    </header>

    <div class="client-container">
      <!-- Форма поиска -->
      <div class="search-form" v-if="!orders.length && !searched">
        <h2>Найдите свои заявки</h2>
        <p>Введите телефон или ссылку ВК, которые вы указывали при оформлении</p>
        
        <div class="form-group">
          <label>Телефон</label>
          <input v-model="searchPhone" type="tel" placeholder="+7 (999) 123-45-67" class="input" />
        </div>
        
        <div class="search-divider">
          <span>или</span>
        </div>
        
        <div class="form-group">
          <label>Ссылка ВКонтакте</label>
          <input v-model="searchVk" type="text" placeholder="https://vk.com/..." class="input" />
        </div>
        
        <button class="btn-primary" @click="searchOrders" :disabled="!searchPhone && !searchVk">
          🔍 Найти заявки
        </button>
      </div>

      <!-- Загрузка -->
      <div v-if="loading" class="loading">
        <div class="spinner"></div>
        <p>Ищем ваши заявки...</p>
      </div>

      <!-- Список заявок -->
      <div v-if="orders.length" class="orders-list">
        <div class="orders-header">
          <h2>Найдено заявок: {{ orders.length }}</h2>
          <button class="btn-secondary" @click="resetSearch">Новый поиск</button>
        </div>

        <div class="order-card" v-for="order in orders" :key="order.id"
          :class="{ processed: order.is_processed }">
          <div class="order-header">
            <span class="order-id">Заявка №{{ order.id }}</span>
            <span class="order-status" :class="{ done: order.is_processed }">
              {{ order.is_processed ? '✅ Выполнена' : '🔄 В работе' }}
            </span>
          </div>
          <div class="order-body">
            <div class="order-info">
              <div class="info-item">
                <span class="info-label">Дата создания</span>
                <span class="info-value">{{ formatDate(order.created_at) }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Страниц</span>
                <span class="info-value">{{ order.pages }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Дедлайн</span>
                <span class="info-value">{{ order.deadline }}</span>
              </div>
              <div class="info-item">
                <span class="info-label">Стоимость</span>
                <span class="info-value price">{{ order.estimated_price }} ₽</span>
              </div>
            </div>
            <div class="order-details">
              <span class="detail-tag">{{ getFormatLabel(order.paper_format) }}</span>
              <span class="detail-tag">{{ getHandwritingLabel(order.handwriting) }}</span>
              <span class="detail-tag" v-if="order.has_tables">📊 Таблицы</span>
              <span class="detail-tag" v-if="order.has_schemes">📐 Схемы</span>
              <span class="detail-tag" v-if="order.has_drawings">🎨 Рисунки</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Ничего не найдено -->
      <div v-if="searched && !orders.length && !loading" class="not-found">
        <div class="not-found-icon">🔍</div>
        <h3>Заявки не найдены</h3>
        <p>Проверьте правильность телефона или ссылки ВК</p>
        <button class="btn-secondary" @click="resetSearch">Попробовать снова</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// URL API — работает и локально, и на Render
const API_URL = import.meta.env.VITE_API_URL || ''

const searchPhone = ref('')
const searchVk = ref('')
const orders = ref([])
const searched = ref(false)
const loading = ref(false)

const FORMATS = {
  'A4_tetrad': 'Тетрадь А4',
  'A5_tetrad': 'Тетрадь А5',
  'A4_list': 'Лист А4',
}

const HANDWRITINGS = {
  'any': 'Обычный почерк',
  'readable': 'Разборчивый',
  'individual': 'Индивидуальный',
}

function getFormatLabel(value) {
  return FORMATS[value] || value
}

function getHandwritingLabel(value) {
  return HANDWRITINGS[value] || value
}

function formatDate(dateStr) {
  if (!dateStr) return ''
  const d = new Date(dateStr)
  return d.toLocaleString('ru-RU', { 
    day: '2-digit', month: '2-digit', year: 'numeric',
    hour: '2-digit', minute: '2-digit'
  })
}

async function searchOrders() {
  if (!searchPhone.value && !searchVk.value) return
  
  loading.value = true
  searched.value = true
  orders.value = []
  
  try {
    const params = new URLSearchParams()
    if (searchPhone.value) params.append('phone', searchPhone.value)
    if (searchVk.value) params.append('vk', searchVk.value)
    
    const response = await fetch(`${API_URL}/api/orders/client/?${params}`)
    const data = await response.json()
    
    if (data.success) {
      orders.value = data.orders
    }
  } catch (e) {
    console.error('Ошибка поиска:', e)
  } finally {
    loading.value = false
  }
}

function resetSearch() {
  orders.value = []
  searched.value = false
  searchPhone.value = ''
  searchVk.value = ''
}
</script>

<style scoped>
.client-page {
  min-height: 100vh;
  background: #faf9f6;
}
.client-header {
  display: flex;
  align-items: center;
  gap: 30px;
  padding: 20px 40px;
  background: white;
  border-bottom: 1px solid #eee;
}
.client-header h1 {
  font-size: 22px;
  color: #1a1a2e;
}
.logo {
  font-size: 16px;
  font-weight: 600;
  color: #4a67d9;
  cursor: pointer;
}
.client-container {
  max-width: 800px;
  margin: 40px auto;
  padding: 0 20px;
}
.search-form {
  background: white;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.06);
  text-align: center;
}
.search-form h2 {
  margin-bottom: 12px;
}
.search-form p {
  color: #888;
  margin-bottom: 30px;
}
.form-group {
  margin-bottom: 20px;
  text-align: left;
}
label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
}
.input {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 16px;
  transition: border 0.3s;
  background: #fafafa;
  box-sizing: border-box;
}
.input:focus {
  border-color: #4a67d9;
  outline: none;
  background: white;
}
.search-divider {
  text-align: center;
  margin: 20px 0;
  color: #ccc;
  position: relative;
}
.search-divider::before,
.search-divider::after {
  content: '';
  position: absolute;
  top: 50%;
  width: 40%;
  height: 1px;
  background: #eee;
}
.search-divider::before { left: 0; }
.search-divider::after { right: 0; }
.search-divider span {
  background: white;
  padding: 0 15px;
  position: relative;
}
.btn-primary {
  width: 100%;
  padding: 16px;
  background: #4a67d9;
  color: white;
  border: none;
  border-radius: 14px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 10px;
}
.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.btn-secondary {
  padding: 10px 20px;
  background: #f0f0f0;
  color: #555;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  font-size: 14px;
}

/* Загрузка */
.loading {
  text-align: center;
  padding: 60px;
}
.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid #eee;
  border-top-color: #4a67d9;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  margin: 0 auto 16px;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Список заявок */
.orders-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.orders-header h2 {
  font-size: 20px;
}
.order-card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 16px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
  border-left: 4px solid #4a67d9;
  transition: transform 0.3s, box-shadow 0.3s;
}
.order-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
}
.order-card.processed {
  border-left-color: #27ae60;
  opacity: 0.85;
}
.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid #eee;
}
.order-id {
  font-weight: 700;
  font-size: 16px;
}
.order-status {
  font-size: 14px;
  font-weight: 600;
  color: #e67e22;
  background: #fff3e0;
  padding: 4px 12px;
  border-radius: 20px;
}
.order-status.done {
  color: #155724;
  background: #d4edda;
}
.order-body {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 20px;
}
.order-info {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px 30px;
}
.info-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.info-label {
  font-size: 12px;
  color: #999;
}
.info-value {
  font-size: 15px;
  font-weight: 600;
}
.info-value.price {
  color: #27ae60;
  font-size: 18px;
}
.order-details {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: flex-start;
  align-content: flex-start;
}
.detail-tag {
  background: #f0f4ff;
  color: #4a67d9;
  padding: 4px 10px;
  border-radius: 8px;
  font-size: 13px;
}

/* Не найдено */
.not-found {
  text-align: center;
  padding: 60px 20px;
  background: white;
  border-radius: 20px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.06);
}
.not-found-icon {
  font-size: 48px;
  margin-bottom: 16px;
}
.not-found h3 {
  margin-bottom: 8px;
}
.not-found p {
  color: #888;
  margin-bottom: 20px;
}
</style>