<script setup>
import { ref, onMounted } from 'vue'

const items = ref([])
const newName = ref("")

// Charger les items
const fetchItems = async () => {
  const response = await fetch("/api/items")
  items.value = await response.json()
}

// Ajouter un item
const addItem = async () => {
  if (!newName.value) return

  const newItem = {
    id: Date.now(),
    name: newName.value
  }

  await fetch("/api/items", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(newItem)
  })

  newName.value = ""
  fetchItems()
}

onMounted(fetchItems)
</script>

<template>
  <div style="max-width: 600px; margin: auto; padding: 20px;">
    <h2>Liste des Items</h2>

    <ul class="items-list">
      <li v-for="item in items" :key="item.code" class="item">
        <!-- Ligne code en entête -->
        <div class="item-header">-------- code : {{ item.code }} --------</div>

        <!-- Autres propriétés -->
        <template v-for="(value, key) in item" :key="key">
          <div v-if="key !== 'code' && key !== 'inputs'" class="item-prop">
            {{ key }} : {{ value }}
          </div>
        </template>

        <!-- Inputs -->
          <div class="inputs-list">
            <div v-for="input in item.inputs" :key="input.code" class="input-item">
              - {{ input.code }} : {{ input.quantity }}
            </div>
          </div>
      </li>
    </ul>

    <hr/>

    <input
        v-model="newName"
        placeholder="Nom du nouvel item"
        style="padding: 5px; margin-right: 10px;"
    />
    <button @click="addItem" style="padding: 5px 10px;">
      Ajouter
    </button>
  </div>
</template>

<style scoped>
.items-list {
  list-style: none;
  padding-left: 0;
  text-align: left; /* Force l'alignement à gauche */
}

.item {
  margin-bottom: 20px;
  text-align: left; /* au cas où un style parent centrerait le texte */
}

.item-header {
  font-weight: bold;
  margin-bottom: 5px;
  text-align: left;
}

.item-prop {
  margin-left: 10px; /* léger décalage pour les propriétés */
  text-align: left;
}

.inputs-header {
  margin-left: 10px;
  font-style: italic;
  margin-top: 5px;
  text-align: left;
}

.inputs-list {
  margin-left: 30px; /* indentation pour les inputs */
  text-align: left;
}

.input-item {
  margin-bottom: 3px;
  text-align: left;
}
</style>