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

        <!-- Инструкция по оплате -->
        <div class="manual-section">
          <h3>📱 Перевод по номеру телефона</h3>
          <div class="phone-box">
            <span class="phone-label">Номер для перевода</span>
            <span class="phone-number">8 996 569-72-85</span>
            <button class="copy-btn" @click="copyPhone">📋 Скопировать</button>
          </div>
          <p class="bank-hint">Сбербанк, Т-Банк, ВТБ, Альфа-Банк и другие</p>
        </div>

        <div class="instruction">
          <h3>⚠️ Обязательно укажите в комментарии к платежу</h3>
          <div class="comment-box">
            <code>Заказ №{{ orderId }}</code>
          </div>
          <p>Сумма к оплате: <strong>{{ price }} ₽</strong></p>
        </div>

        <div class="next-steps">
          <h3>Что дальше?</h3>
          <p>✅ После поступления оплаты мы свяжемся с вами в VK для подтверждения заказа.</p>
          <p>⏰ График работы: Пн–Вс с 10:00 до 23:00.</p>
          <p>💬 Убедитесь, что ваши личные сообщения в VK открыты.</p>
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
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const orderId = ref(route.query.orderId || '—')
const price = ref(route.query.price || '0')

function copyPhone() {
  navigator.clipboard.writeText('89965697285')
    .then(() => alert('Номер скопирован!'))
    .catch(() => prompt('Скопируйте номер:', '89965697285'))
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
.manual-section { margin-bottom: 24px; }
.manual-section h3 { margin-bottom: 12px; }
.phone-box { padding: 20px; background: #f0f4ff; border-radius: 16px; border: 2px solid #4a67d9; }
.phone-label { font-size: 13px; color: #888; display: block; margin-bottom: 6px; }
.phone-number { font-size: 26px; font-weight: 800; color: #1a1a2e; letter-spacing: 1px; }
.copy-btn { background: #4a67d9; color: white; border: none; padding: 10px 20px; border-radius: 10px; cursor: pointer; margin-top: 10px; font-size: 14px; }
.copy-btn:hover { background: #3a54c0; }
.bank-hint { font-size: 13px; color: #999; margin-top: 10px; }
.instruction { background: #fff3cd; padding: 24px; border-radius: 16px; margin-bottom: 24px; text-align: left; }
.instruction h3 { margin-bottom: 14px; font-size: 16px; }
.comment-box { background: white; padding: 16px; border-radius: 10px; margin: 12px 0; text-align: center; border: 2px dashed #ffc107; }
.comment-box code { font-size: 20px; font-weight: 700; color: #1a1a2e; }
.next-steps { background: #eafaf1; padding: 24px; border-radius: 16px; margin-bottom: 24px; text-align: left; }
.next-steps h3 { margin-bottom: 14px; font-size: 16px; }
.next-steps p { font-size: 14px; color: #155724; margin: 8px 0; }
.btn-row { display: flex; gap: 12px; }
.btn-primary, .btn-vk { flex: 1; padding: 16px; border: none; border-radius: 14px; font-size: 16px; font-weight: 600; cursor: pointer; text-align: center; text-decoration: none; }
.btn-primary { background: #f0f0f0; color: #555; }
.btn-vk { background: #4a67d9; color: white; }
@media (max-width: 500px) {
  .payment-card { padding: 20px; }
  .btn-row { flex-direction: column; }
}
</style>