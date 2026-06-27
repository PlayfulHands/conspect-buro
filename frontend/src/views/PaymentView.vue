<template>
  <div class="payment-page">
    <header class="payment-header">
      <div class="logo" @click="$router.push('/')">← На главную</div>
      <h1>Оплата заказа</h1>
    </header>

    <div class="payment-container">
      <div class="payment-card">
        <div class="order-badge">
          Заказ №{{ orderId }} · {{ price }} ₽
        </div>

        <h2>Для завершения заказа переведите оплату</h2>

        <!-- QR-код -->
        <div class="qr-section">
          <p class="qr-hint">Отсканируйте QR-код камерой телефона или через приложение банка</p>
          <img 
            :src="qrDataUrl" 
            alt="QR-код для оплаты" 
            class="qr-image"
            v-if="qrDataUrl"
          />
          <p v-else class="qr-loading">Загрузка QR-кода...</p>
        </div>

        <div class="divider">
          <span>или</span>
        </div>

        <!-- Ручной перевод -->
        <div class="manual-section">
          <h3>Переведите вручную</h3>
          <div class="phone-box">
            <span class="phone-label">Номер для перевода</span>
            <span class="phone-number">8 999 656-97-28</span>
            <button class="copy-btn" @click="copyPhone">📋 Скопировать</button>
          </div>
        </div>

        <!-- Инструкция -->
        <div class="instruction">
          <h3>⚠️ Важно</h3>
          <p>При переводе обязательно укажите в комментарии к платежу:</p>
          <div class="comment-box">
            <code>Заказ №{{ orderId }}</code>
          </div>
          <p class="instruction-hint">Это нужно, чтобы мы могли идентифицировать ваш платёж и начать работу над заказом.</p>
        </div>

        <!-- Что дальше -->
        <div class="next-steps">
          <h3>Что дальше?</h3>
          <p>✅ После поступления оплаты мы свяжемся с вами в VK для подтверждения заказа.</p>
          <p>⏰ График работы: Пн–Вс с 10:00 до 23:00.</p>
          <p>💬 Убедитесь, что личные сообщения в VK открыты.</p>
        </div>

        <div class="btn-row">
          <button class="btn-primary" @click="$router.push('/')">Вернуться на главную</button>
          <a href="https://vk.com/konspektps" target="_blank" class="btn-vk">Написать в VK</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const orderId = ref(route.query.orderId || '—')
const price = ref(route.query.price || '0')
const qrDataUrl = ref('')

onMounted(async () => {
  const text = `ST00012|Name=Конспект Бюро|PersonalAcc=89965697285|BankName=СБЕРБАНК|Sum=${price.value * 100}|Purpose=Заказ №${orderId.value}`
  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=220x220&data=${encodeURIComponent(text)}`
  qrDataUrl.value = qrUrl
})

function copyPhone() {
  navigator.clipboard.writeText('89965697285').then(() => {
    alert('Номер скопирован!')
  }).catch(() => {
    prompt('Скопируйте номер:', '89965697285')
  })
}
</script>

<style scoped>
.payment-page { min-height: 100vh; background: #faf9f6; }
.payment-header { display: flex; align-items: center; gap: 30px; padding: 20px 40px; background: white; border-bottom: 1px solid #eee; }
.payment-header h1 { font-size: 22px; }
.logo { font-size: 16px; font-weight: 600; color: #4a67d9; cursor: pointer; }
.payment-container { max-width: 600px; margin: 40px auto; padding: 0 20px; }
.payment-card { background: white; border-radius: 20px; padding: 40px; box-shadow: 0 2px 16px rgba(0,0,0,0.06); text-align: center; }
.order-badge { display: inline-block; background: #f0f4ff; color: #4a67d9; padding: 10px 24px; border-radius: 30px; font-weight: 700; font-size: 18px; margin-bottom: 24px; }
h2 { font-size: 22px; margin-bottom: 24px; }
.qr-section { margin-bottom: 24px; }
.qr-hint { color: #888; margin-bottom: 16px; font-size: 14px; }
.qr-image { display: inline-block; padding: 16px; background: white; border: 2px solid #eee; border-radius: 12px; max-width: 260px; }
.qr-loading { color: #999; padding: 40px; }
.divider { text-align: center; margin: 24px 0; color: #ccc; position: relative; }
.divider::before, .divider::after { content: ''; position: absolute; top: 50%; width: 40%; height: 1px; background: #eee; }
.divider::before { left: 0; } .divider::after { right: 0; }
.divider span { background: white; padding: 0 16px; position: relative; }
.manual-section { margin-bottom: 24px; }
.manual-section h3 { margin-bottom: 12px; }
.phone-box { display: flex; align-items: center; justify-content: center; gap: 12px; flex-wrap: wrap; padding: 16px; background: #faf9f6; border-radius: 12px; }
.phone-label { font-size: 13px; color: #888; width: 100%; }
.phone-number { font-size: 22px; font-weight: 700; letter-spacing: 1px; }
.copy-btn { background: #f0f0f0; border: none; padding: 8px 16px; border-radius: 8px; cursor: pointer; font-size: 14px; }
.instruction { background: #fff3cd; padding: 20px; border-radius: 12px; margin-bottom: 24px; text-align: left; }
.instruction h3 { margin-bottom: 12px; }
.comment-box { background: white; padding: 12px; border-radius: 8px; margin: 10px 0; text-align: center; }
.comment-box code { font-size: 18px; font-weight: 700; color: #1a1a2e; }
.instruction-hint { font-size: 13px; color: #856404; margin-top: 8px; }
.next-steps { background: #eafaf1; padding: 20px; border-radius: 12px; margin-bottom: 24px; text-align: left; }
.next-steps h3 { margin-bottom: 12px; }
.next-steps p { font-size: 14px; color: #155724; margin: 6px 0; }
.btn-row { display: flex; gap: 12px; }
.btn-primary, .btn-vk { flex: 1; padding: 16px; border: none; border-radius: 14px; font-size: 16px; font-weight: 600; cursor: pointer; text-align: center; text-decoration: none; }
.btn-primary { background: #f0f0f0; color: #555; }
.btn-vk { background: #4a67d9; color: white; }
@media (max-width: 500px) {
  .payment-card { padding: 20px; }
  .btn-row { flex-direction: column; }
}
</style>