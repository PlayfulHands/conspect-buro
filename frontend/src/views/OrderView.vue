<template>
  <div class="order-page">
    <!-- Шапка -->
    <header class="order-header">
      <div class="logo" @click="$router.push('/')">← На главную</div>
      <div class="steps-indicator">
        <div class="step-dot" :class="{ active: step >= 1, completed: step > 1 }">1</div>
        <div class="step-line" :class="{ active: step > 1 }"></div>
        <div class="step-dot" :class="{ active: step >= 2, completed: step > 2 }">2</div>
        <div class="step-line" :class="{ active: step > 2 }"></div>
        <div class="step-dot" :class="{ active: step >= 3 }">3</div>
      </div>
    </header>

    <div class="order-container">
      <!-- Боковая панель с ценой (видна всегда) -->
      <aside class="price-sidebar">
        <div class="price-card">
          <div class="price-label">Ориентировочная стоимость</div>
          <div class="price-value">{{ calculatedPrice }} ₽</div>
          <div class="price-breakdown" v-if="step >= 2">
            <div class="breakdown-item" v-if="basePrice > 0">
              <span>Базовая цена ({{ form.pages }} стр.)</span>
              <span>{{ basePrice }} ₽</span>
            </div>
            <div class="breakdown-item" v-if="form.paper_format !== 'A4_tetrad'">
              <span>Формат ({{ formatLabel }})</span>
              <span>×{{ formatMultiplier }}</span>
            </div>
            <div class="breakdown-item" v-if="form.handwriting !== 'any'">
              <span>Почерк ({{ handwritingLabel }})</span>
              <span>×{{ handwritingMultiplier }}</span>
            </div>
            <div class="breakdown-item urgency" v-if="urgencyMultiplier > 1">
              <span>Срочность ({{ urgencyDays }} дн.)</span>
              <span>×{{ urgencyMultiplier }}</span>
            </div>
            <div class="breakdown-item" v-if="extrasTotal > 0">
              <span>Доп. элементы</span>
              <span>+{{ extrasTotal }} ₽</span>
            </div>
          </div>
          <div class="urgency-warning" v-if="urgencyMultiplier >= 2">
            ⚡ Срочный заказ — цена увеличена
          </div>
          <div class="price-hint" v-if="step < 2">
            Заполните параметры работы для расчёта
          </div>
        </div>
        
        <!-- Блок "Как считается цена" -->
        <details class="pricing-info">
          <summary>Как рассчитывается стоимость?</summary>
          <div class="pricing-info-content">
            <p><strong>Объём:</strong> 500 ₽ за первую стр. + 150 ₽ за каждую следующую</p>
            <p><strong>Формат:</strong> А4×1, А5×0.8, Лист×0.6</p>
            <p><strong>Почерк:</strong> обычный×1, разборчивый×1.2, индив.×1.5</p>
            <p><strong>Сроки:</strong> 4+ дн×1, 2-3 дн×1.5, 1 дн×2</p>
            <p><strong>Элементы:</strong> таблицы/схемы +150 ₽, рисунки +200 ₽</p>
          </div>
        </details>
      </aside>

      <!-- Форма -->
      <main class="form-area">
        <!-- Шаг 1 -->
        <div v-if="step === 1" class="form-step">
          <span class="step-badge">Шаг 1 из 3</span>
          <h2>Контакты и основа</h2>
          <p class="step-desc">Оставьте свои данные для связи. Мы не передаём их третьим лицам.</p>
          
          <div class="form-group">
            <label>Ссылка ВКонтакте <span class="required">*</span></label>
            <input v-model="form.vk_link" type="url" placeholder="https://vk.com/ваш_профиль" class="input" />
            <span class="field-hint">Нужна для связи с вами</span>
          </div>
          
          <div class="form-group">
            <label>Номер телефона <span class="required">*</span></label>
            <input v-model="form.phone" type="tel" placeholder="+7 (999) 123-45-67" class="input" />
          </div>
          
          <div class="form-group">
            <label>Способ получения <span class="required">*</span></label>
            <div class="radio-cards">
              <label class="radio-card" :class="{ selected: form.get_type === 'pickup' }">
                <input type="radio" v-model="form.get_type" value="pickup" />
                <span class="radio-icon">🤝</span>
                <span class="radio-title">Заберу сам</span>
              </label>
              <label class="radio-card" :class="{ selected: form.get_type === 'delivery' }">
                <input type="radio" v-model="form.get_type" value="delivery" />
                <span class="radio-icon">📦</span>
                <span class="radio-title">Нужна доставка</span>
              </label>
            </div>
          </div>
          
          <button class="btn-primary" @click="nextStep" :disabled="!step1Valid">
            Далее → Параметры работы
          </button>
        </div>

        <!-- Шаг 2 -->
        <div v-if="step === 2" class="form-step">
          <span class="step-badge">Шаг 2 из 3</span>
          <h2>Параметры работы</h2>
          <p class="step-desc">От этих параметров зависит итоговая стоимость. Слева вы видите, как меняется цена.</p>
          
          <div class="form-group">
            <label>Объём работы (количество страниц) <span class="required">*</span></label>
            <div class="input-with-suffix">
              <input v-model.number="form.pages" type="number" min="1" max="200" class="input" placeholder="10" />
              <span class="suffix">стр.</span>
            </div>
            <span class="field-hint">От 1 до 200 страниц</span>
          </div>
          
          <div class="form-group">
            <label>Срок сдачи <span class="required">*</span></label>
            <input v-model="form.deadline" type="date" class="input" :min="minDate" />
            <div class="urgency-info" v-if="urgencyMultiplier > 1">
              <span v-if="urgencyMultiplier >= 2" class="urgency-tag hot">⚡ Срочно! ×2 к цене</span>
              <span v-else class="urgency-tag warm">🔥 Ускоренно ×1.5 к цене</span>
            </div>
          </div>
          
          <div class="form-group">
            <label>Формат <span class="required">*</span></label>
            <div class="radio-cards">
              <label class="radio-card" v-for="fmt in formats" :key="fmt.value"
                :class="{ selected: form.paper_format === fmt.value }">
                <input type="radio" v-model="form.paper_format" :value="fmt.value" />
                <span class="radio-icon">{{ fmt.icon }}</span>
                <span class="radio-title">{{ fmt.label }}</span>
                <span class="radio-price">{{ fmt.priceLabel }}</span>
              </label>
            </div>
          </div>
          
          <div class="form-group">
            <label>Требования к почерку <span class="required">*</span></label>
            <div class="radio-cards">
              <label class="radio-card" v-for="hw in handwritings" :key="hw.value"
                :class="{ selected: form.handwriting === hw.value }">
                <input type="radio" v-model="form.handwriting" :value="hw.value" />
                <span class="radio-icon">{{ hw.icon }}</span>
                <span class="radio-title">{{ hw.label }}</span>
                <span class="radio-price">{{ hw.priceLabel }}</span>
              </label>
            </div>
          </div>
          
          <div class="btn-row">
            <button class="btn-secondary" @click="prevStep">← Назад</button>
            <button class="btn-primary" @click="nextStep" :disabled="!step2Valid">
              Далее → Детали
            </button>
          </div>
        </div>

        <!-- Шаг 3 -->
        <div v-if="step === 3" class="form-step">
          <span class="step-badge">Шаг 3 из 3</span>
          <h2>Детали и подтверждение</h2>
          
          <div class="form-group">
            <label>Наличие исходного материала <span class="required">*</span></label>
            <div class="radio-cards">
              <label class="radio-card" :class="{ selected: form.has_material === 'yes' }">
                <input type="radio" v-model="form.has_material" value="yes" />
                <span class="radio-icon">✅</span>
                <span class="radio-title">Есть готовый</span>
              </label>
              <label class="radio-card" :class="{ selected: form.has_material === 'soon' }">
                <input type="radio" v-model="form.has_material" value="soon" />
                <span class="radio-icon">⏳</span>
                <span class="radio-title">Скоро появится</span>
              </label>
            </div>
          </div>
          
          <div class="form-group">
            <label>Дополнительные элементы</label>
            <div class="checkbox-cards">
              <label class="checkbox-card" :class="{ checked: form.has_tables }">
                <input type="checkbox" v-model="form.has_tables" />
                <span class="checkbox-icon">📊</span>
                <span>Таблицы</span>
                <span class="checkbox-price">+150 ₽</span>
              </label>
              <label class="checkbox-card" :class="{ checked: form.has_schemes }">
                <input type="checkbox" v-model="form.has_schemes" />
                <span class="checkbox-icon">📐</span>
                <span>Схемы</span>
                <span class="checkbox-price">+150 ₽</span>
              </label>
              <label class="checkbox-card" :class="{ checked: form.has_drawings }">
                <input type="checkbox" v-model="form.has_drawings" />
                <span class="checkbox-icon">🎨</span>
                <span>Рисунки</span>
                <span class="checkbox-price">+200 ₽</span>
              </label>
              <label class="checkbox-card" :class="{ checked: form.text_only }">
                <input type="checkbox" v-model="form.text_only" />
                <span class="checkbox-icon">📝</span>
                <span>Только текст</span>
                <span class="checkbox-price">0 ₽</span>
              </label>
            </div>
          </div>

          <!-- ЗАГРУЗКА ФАЙЛА -->
          <div class="form-group">
            <label>Исходный материал (файл)</label>
            <div class="file-upload">
              <label class="file-label" :class="{ 'has-file': uploadedFile }">
                <span v-if="!uploadedFile">📎 Прикрепить файл</span>
                <span v-else>📄 {{ uploadedFile.name }}</span>
                <input type="file" @change="handleFileUpload" class="file-input" 
                  accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.txt" />
              </label>
              <button v-if="uploadedFile" @click="removeFile" class="btn-remove-file" type="button">✕</button>
            </div>
            <span class="field-hint">PDF, Word, изображения, текст (до 10 МБ)</span>
          </div>
          
          <div class="form-group">
            <label>Дополнительная информация</label>
            <textarea v-model="form.additional_info" rows="4" class="textarea" 
              placeholder="Особые требования к оформлению, почерку и т.д. Если их нет, поставьте точку"></textarea>
          </div>

          <!-- Итоговый блок -->
          <div class="final-summary">
            <h3>Проверьте заказ</h3>
            <div class="summary-list">
              <div class="summary-row"><span>ВК:</span><span>{{ form.vk_link || '—' }}</span></div>
              <div class="summary-row"><span>Телефон:</span><span>{{ form.phone || '—' }}</span></div>
              <div class="summary-row"><span>Объём:</span><span>{{ form.pages }} стр.</span></div>
              <div class="summary-row"><span>Срок:</span><span>{{ form.deadline || '—' }}</span></div>
              <div class="summary-row"><span>Формат:</span><span>{{ formatLabel }}</span></div>
              <div class="summary-row"><span>Почерк:</span><span>{{ handwritingLabel }}</span></div>
              <div class="summary-row"><span>Получение:</span><span>{{ form.get_type === 'pickup' ? 'Заберу сам' : 'Доставка' }}</span></div>
              <div class="summary-row" v-if="uploadedFile"><span>Файл:</span><span>{{ uploadedFile.name }}</span></div>
              <div class="summary-row total-row"><span>Итого:</span><span>{{ calculatedPrice }} ₽</span></div>
            </div>
          </div>
          
          <!-- Сообщения об успехе/ошибке -->
          <div v-if="successMessage" class="success-message">
            <span>✅</span> 
            <div>
              {{ successMessage }}
              <br>
              <router-link to="/client" class="client-link">Отслеживать статус заявки →</router-link>
            </div>
          </div>
          <div v-if="errorMessage" class="error-message">
            <span>❌</span> {{ errorMessage }}
          </div>
          
          <div class="btn-row">
            <button class="btn-secondary" @click="prevStep">← Назад</button>
            <button class="btn-primary btn-submit" @click="submitOrder" :disabled="submitting || !step3Valid">
              {{ submitting ? 'Отправка...' : 'Отправить заявку' }}
            </button>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'

// URL API — работает и локально, и на Render
const API_URL = import.meta.env.VITE_API_URL || ''

const step = ref(1)
const submitting = ref(false)
const successMessage = ref('')
const errorMessage = ref('')
const uploadedFile = ref(null)

const form = reactive({
  vk_link: '',
  phone: '',
  pages: 10,
  deadline: '',
  paper_format: 'A4_tetrad',
  handwriting: 'any',
  has_material: 'yes',
  has_tables: false,
  has_schemes: false,
  has_drawings: false,
  text_only: false,
  additional_info: '.',
  get_type: 'pickup',
})

const formats = [
  { value: 'A4_tetrad', label: 'Тетрадь А4', icon: '📒', priceLabel: '×1' },
  { value: 'A5_tetrad', label: 'Тетрадь А5', icon: '📔', priceLabel: '×0.8' },
  { value: 'A4_list', label: 'Лист А4', icon: '📄', priceLabel: '×0.6' },
]

const handwritings = [
  { value: 'any', label: 'Не имеет значения', icon: '✍️', priceLabel: '×1' },
  { value: 'readable', label: 'Разборчивый', icon: '✨', priceLabel: '×1.2' },
  { value: 'individual', label: 'Индивидуальный подбор', icon: '🎯', priceLabel: '×1.5' },
]

const minDate = computed(() => {
  const tomorrow = new Date()
  tomorrow.setDate(tomorrow.getDate() + 1)
  return tomorrow.toISOString().split('T')[0]
})

const step1Valid = computed(() => {
  return form.vk_link.trim() && form.phone.trim() && form.get_type
})

const step2Valid = computed(() => {
  return form.pages > 0 && form.pages <= 200 && form.deadline && form.paper_format && form.handwriting
})

const step3Valid = computed(() => {
  return form.has_material
})

const basePrice = computed(() => {
  if (form.pages <= 0) return 0
  return 500 + (form.pages - 1) * 150
})

const formatMultiplier = computed(() => {
  const m = { 'A4_tetrad': 1, 'A5_tetrad': 0.8, 'A4_list': 0.6 }
  return m[form.paper_format] || 1
})

const handwritingMultiplier = computed(() => {
  const m = { 'any': 1, 'readable': 1.2, 'individual': 1.5 }
  return m[form.handwriting] || 1
})

const urgencyDays = computed(() => {
  if (!form.deadline) return 999
  return Math.ceil((new Date(form.deadline) - new Date()) / (1000 * 60 * 60 * 24))
})

const urgencyMultiplier = computed(() => {
  if (urgencyDays.value <= 1) return 2
  if (urgencyDays.value <= 3) return 1.5
  return 1
})

const extrasTotal = computed(() => {
  let total = 0
  if (form.has_tables) total += 150
  if (form.has_schemes) total += 150
  if (form.has_drawings) total += 200
  return total
})

const calculatedPrice = computed(() => {
  let price = basePrice.value
  price = price * formatMultiplier.value
  price = price * handwritingMultiplier.value
  price = price * urgencyMultiplier.value
  price = Math.round(price + extrasTotal.value)
  return price
})

const formatLabel = computed(() => formats.find(f => f.value === form.paper_format)?.label || '')
const handwritingLabel = computed(() => handwritings.find(h => h.value === form.handwriting)?.label || '')

function nextStep() { step.value++ }
function prevStep() { step.value-- }

function handleFileUpload(event) {
  const file = event.target.files[0]
  if (file && file.size <= 10 * 1024 * 1024) {
    uploadedFile.value = file
  } else if (file) {
    alert('Файл слишком большой. Максимальный размер — 10 МБ.')
  }
}

function removeFile() {
  uploadedFile.value = null
}

async function submitOrder() {
  submitting.value = true
  errorMessage.value = ''
  successMessage.value = ''

  try {
    const formData = new FormData()
    
    Object.keys(form).forEach(key => {
      formData.append(key, form[key])
    })
    formData.append('estimated_price', calculatedPrice.value)
    
    if (uploadedFile.value) {
      formData.append('uploaded_file', uploadedFile.value)
    }

    const response = await fetch(`${API_URL}/api/orders/create/`, {
      method: 'POST',
      body: formData,
    })
    
    const data = await response.json()
    
    if (response.ok) {
      successMessage.value = data.message || 'Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.'
    } else {
      errorMessage.value = 'Ошибка: ' + JSON.stringify(data.errors || data)
    }
  } catch (e) {
    errorMessage.value = 'Не удалось отправить заявку. Проверьте соединение с сервером.'
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.order-page {
  min-height: 100vh;
  background: #faf9f6;
}

.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  background: white;
  border-bottom: 1px solid #eee;
}
.logo {
  font-size: 16px;
  font-weight: 600;
  color: #4a67d9;
  cursor: pointer;
}
.steps-indicator {
  display: flex;
  align-items: center;
  gap: 0;
}
.step-dot {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 14px;
  background: #eee;
  color: #999;
  transition: all 0.3s;
}
.step-dot.active {
  background: #4a67d9;
  color: white;
}
.step-dot.completed {
  background: #d4edda;
  color: #155724;
}
.step-line {
  width: 40px;
  height: 2px;
  background: #eee;
  transition: background 0.3s;
}
.step-line.active {
  background: #4a67d9;
}

.order-container {
  display: flex;
  max-width: 1200px;
  margin: 40px auto;
  gap: 30px;
  padding: 0 20px;
}

.price-sidebar {
  width: 320px;
  flex-shrink: 0;
  position: sticky;
  top: 100px;
  align-self: flex-start;
}
.price-card {
  background: white;
  border-radius: 16px;
  padding: 30px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.06);
  text-align: center;
  margin-bottom: 16px;
}
.price-label {
  font-size: 14px;
  color: #999;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 1px;
}
.price-value {
  font-size: 42px;
  font-weight: 800;
  color: #1a1a2e;
  margin-bottom: 20px;
}
.price-breakdown {
  text-align: left;
  border-top: 1px solid #eee;
  padding-top: 16px;
}
.breakdown-item {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
  color: #666;
  padding: 4px 0;
}
.breakdown-item.urgency {
  color: #e67e22;
}
.urgency-warning {
  background: #fff3cd;
  color: #856404;
  padding: 10px;
  border-radius: 8px;
  margin-top: 16px;
  font-size: 14px;
  font-weight: 600;
}
.price-hint {
  color: #bbb;
  font-size: 14px;
  margin-top: 16px;
}
.pricing-info {
  background: white;
  border-radius: 16px;
  padding: 16px 20px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.06);
  cursor: pointer;
}
.pricing-info summary {
  font-size: 14px;
  color: #4a67d9;
  font-weight: 600;
  list-style: none;
}
.pricing-info-content {
  margin-top: 12px;
  font-size: 13px;
  color: #666;
}
.pricing-info-content p {
  margin: 6px 0;
}

.form-area {
  flex: 1;
  background: white;
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 2px 16px rgba(0,0,0,0.06);
}
.form-step {
  animation: fadeIn 0.3s ease;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}
.step-badge {
  display: inline-block;
  background: #f0f4ff;
  color: #4a67d9;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 16px;
}
h2 {
  font-size: 28px;
  margin-bottom: 8px;
  color: #1a1a2e;
}
.step-desc {
  color: #888;
  margin-bottom: 30px;
  font-size: 15px;
}
.form-group {
  margin-bottom: 24px;
}
label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  font-size: 15px;
  color: #333;
}
.required {
  color: #e74c3c;
}
.input, .textarea {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e0e0e0;
  border-radius: 12px;
  font-size: 16px;
  transition: border 0.3s, box-shadow 0.3s;
  background: #fafafa;
  font-family: inherit;
  box-sizing: border-box;
}
.input:focus, .textarea:focus {
  border-color: #4a67d9;
  box-shadow: 0 0 0 3px rgba(74, 103, 217, 0.1);
  background: white;
  outline: none;
}
.input-with-suffix {
  display: flex;
  align-items: center;
}
.input-with-suffix .input {
  border-radius: 12px 0 0 12px;
}
.suffix {
  background: #eee;
  padding: 14px 16px;
  border-radius: 0 12px 12px 0;
  color: #666;
  font-weight: 600;
}
.field-hint {
  display: block;
  margin-top: 6px;
  font-size: 13px;
  color: #aaa;
}
.urgency-info {
  margin-top: 8px;
}
.urgency-tag {
  display: inline-block;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 13px;
  font-weight: 600;
}
.urgency-tag.hot {
  background: #ffeaea;
  color: #c0392b;
}
.urgency-tag.warm {
  background: #fff3e0;
  color: #e67e22;
}

.file-upload {
  display: flex;
  align-items: center;
  gap: 12px;
}
.file-label {
  display: inline-block;
  padding: 14px 24px;
  background: #f0f4ff;
  border: 2px dashed #b0c4f0;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s;
  font-weight: 500;
  color: #4a67d9;
  text-align: center;
  flex: 1;
}
.file-label:hover {
  background: #e0eaff;
  border-color: #4a67d9;
}
.file-label.has-file {
  background: #eafaf1;
  border-color: #27ae60;
  border-style: solid;
  color: #155724;
}
.file-input {
  display: none;
}
.btn-remove-file {
  background: #ffeaea;
  color: #c0392b;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
}
.btn-remove-file:hover {
  background: #fdd;
}

.radio-cards, .checkbox-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 12px;
}
.radio-card, .checkbox-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  padding: 16px 12px;
  border: 2px solid #e0e0e0;
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.3s;
  text-align: center;
}
.radio-card:hover, .checkbox-card:hover {
  border-color: #b0c4f0;
}
.radio-card.selected, .checkbox-card.checked {
  border-color: #4a67d9;
  background: #f0f4ff;
}
.radio-card input, .checkbox-card input {
  display: none;
}
.radio-icon, .checkbox-icon {
  font-size: 28px;
}
.radio-title, .checkbox-title {
  font-weight: 600;
  font-size: 14px;
  color: #333;
}
.radio-price, .checkbox-price {
  font-size: 13px;
  color: #4a67d9;
  font-weight: 600;
}

.final-summary {
  background: #f9fafb;
  border-radius: 14px;
  padding: 24px;
  margin: 24px 0;
}
.final-summary h3 {
  margin-bottom: 16px;
  color: #1a1a2e;
}
.summary-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.summary-row {
  display: flex;
  justify-content: space-between;
  font-size: 15px;
  color: #555;
}
.summary-row.total-row {
  border-top: 1px solid #ddd;
  padding-top: 10px;
  margin-top: 4px;
  font-weight: 700;
  font-size: 18px;
  color: #1a1a2e;
}

.btn-row {
  display: flex;
  gap: 16px;
  margin-top: 30px;
}
.btn-primary {
  flex: 1;
  padding: 16px 28px;
  background: #4a67d9;
  color: white;
  border: none;
  border-radius: 14px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}
.btn-primary:hover:not(:disabled) {
  background: #3a54c0;
  transform: translateY(-1px);
}
.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.btn-secondary {
  padding: 16px 28px;
  background: #f0f0f0;
  color: #555;
  border: none;
  border-radius: 14px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
}
.btn-secondary:hover {
  background: #e0e0e0;
}
.btn-submit {
  background: #27ae60;
}
.btn-submit:hover:not(:disabled) {
  background: #219a52;
}

.success-message {
  background: #d4edda;
  color: #155724;
  padding: 16px 20px;
  border-radius: 12px;
  margin-top: 20px;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-weight: 500;
}
.error-message {
  background: #f8d7da;
  color: #721c24;
  padding: 16px 20px;
  border-radius: 12px;
  margin-top: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 500;
}
.client-link {
  color: #155724;
  font-weight: 700;
  margin-top: 4px;
  display: inline-block;
}
.client-link:hover {
  text-decoration: underline;
}

@media (max-width: 900px) {
  .order-container {
    flex-direction: column;
    margin: 20px auto;
  }
  .price-sidebar {
    width: 100%;
    position: static;
    order: -1;
  }
  .price-value {
    font-size: 32px;
  }
  .form-area {
    padding: 24px;
  }
  .radio-cards {
    grid-template-columns: 1fr 1fr;
  }
  .checkbox-cards {
    grid-template-columns: 1fr 1fr;
  }
}
</style>