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

        <!-- Блок с номером телефона -->
        <div class="phone-section">
          <div class="phone-icon">📱</div>
          <p class="phone-label">Перевод по номеру телефона</p>
          <div class="phone-number">8 996 569-72-85</div>
          <button class="copy-btn" @click="copyPhone">
            📋 Скопировать номер
          </button>
          <p class="phone-hint">Сбербанк, Т-Банк, ВТБ, Альфа-Банк и другие</p>
        </div>

        <!-- Инструкция -->
        <div class="instruction">
          <h3>⚠️ Обязательно укажите в комментарии</h3>
          <div class="comment-box">
            <code>Заказ №{{ orderId }}</code>
          </div>
          <p class="instruction-sum">Сумма к оплате: <strong>{{ price }} ₽</strong></p>
        </div>

        <!-- Что дальше -->
        <div class="next-steps">
          <h3>Что дальше?</h3>
          <p>✅ После поступления оплаты мы свяжемся с вами в VK для подтверждения заказа.</p>
          <p>⏰ График работы: Пн–Вс с 10:00 до 23:00.</p>
          <p>💬 Убедитесь, что ваши личные сообщения в VK открыты.</p>
        </div>

        <div class="btn-row">
          <button class="btn-home" @click="$router.push('/')">Вернуться на главную</button>
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
.payment-page {
  min-height: 100vh;
  background: linear-gradient(180deg, #f0f4ff 0%, #faf9f6 100%);
}

.payment-header {
  display: flex;
  align-items: center;
  gap: 30px;
  padding: 20px 40px;
  background: white;
  border-bottom: 1px solid #eee;
}
.payment-header h1 {
  font-size: 22px;
  color: #1a1a2e;
}
.logo {
  font-size: 16px;
  font-weight: 600;
  color: #4a67d9;
  cursor: pointer;
  transition: color 0.3s;
}
.logo:hover {
  color: #3a54c0;
}

.payment-container {
  max-width: 550px;
  margin: 40px auto;
  padding: 0 20px;
}

.payment-card {
  background: white;
  border-radius: 24px;
  padding: 40px 36px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.06);
  text-align: center;
}

.order-badge {
  display: inline-block;
  background: #f0f4ff;
  color: #4a67d9;
  padding: 10px 24px;
  border-radius: 30px;
  font-weight: 700;
  font-size: 18px;
  margin-bottom: 28px;
}

h2 {
  font-size: 20px;
  margin-bottom: 28px;
  color: #1a1a2e;
  font-weight: 700;
}

/* Блок с номером */
.phone-section {
  background: linear-gradient(135deg, #f0f4ff, #e8eeff);
  border: 2px solid #4a67d9;
  border-radius: 20px;
  padding: 30px 20px;
  margin-bottom: 24px;
}
.phone-icon {
  font-size: 40px;
  margin-bottom: 12px;
}
.phone-label {
  font-size: 14px;
  color: #888;
  margin-bottom: 10px;
}
.phone-number {
  font-size: 30px;
  font-weight: 800;
  color: #1a1a2e;
  letter-spacing: 2px;
  margin-bottom: 16px;
}
.copy-btn {
  background: #4a67d9;
  color: white;
  border: none;
  padding: 12px 28px;
  border-radius: 12px;
  cursor: pointer;
  font-size: 15px;
  font-weight: 600;
  transition: all 0.3s;
}
.copy-btn:hover {
  background: #3a54c0;
  transform: translateY(-1px);
}
.phone-hint {
  font-size: 12px;
  color: #999;
  margin-top: 14px;
}

/* Инструкция */
.instruction {
  background: #fffdf5;
  border: 1px solid #ffe082;
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 24px;
  text-align: left;
}
.instruction h3 {
  margin-bottom: 14px;
  font-size: 16px;
  color: #e67e22;
}
.comment-box {
  background: white;
  padding: 16px;
  border-radius: 10px;
  margin: 12px 0;
  text-align: center;
  border: 2px dashed #ffc107;
}
.comment-box code {
  font-size: 20px;
  font-weight: 700;
  color: #1a1a2e;
}
.instruction-sum {
  text-align: center;
  font-size: 16px;
  margin-top: 8px;
  color: #555;
}
.instruction-sum strong {
  color: #27ae60;
  font-size: 20px;
}

/* Что дальше */
.next-steps {
  background: #eafaf1;
  border-radius: 16px;
  padding: 24px;
  margin-bottom: 24px;
  text-align: left;
}
.next-steps h3 {
  margin-bottom: 14px;
  font-size: 16px;
  color: #155724;
}
.next-steps p {
  font-size: 14px;
  color: #2d6a4f;
  margin: 8px 0;
}

/* Кнопки */
.btn-row {
  display: flex;
  gap: 12px;
}
.btn-home, .btn-vk {
  flex: 1;
  padding: 16px;
  border: none;
  border-radius: 14px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  transition: all 0.3s;
}
.btn-home {
  background: #f0f0f0;
  color: #555;
}
.btn-home:hover {
  background: #e0e0e0;
}
.btn-vk {
  background: #4a67d9;
  color: white;
}
.btn-vk:hover {
  background: #3a54c0;
}

@media (max-width: 500px) {
  .payment-card {
    padding: 24px 16px;
  }
  .phone-number {
    font-size: 24px;
  }
  .btn-row {
    flex-direction: column;
  }
}
</style>