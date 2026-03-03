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
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(newItem)
  })

  newName.value = ""
  fetchItems()
}

onMounted(fetchItems)
</script>

<template>
  <div style="max-width: 400px; margin: auto; padding: 20px;">
    <h2>Liste des Items</h2>

    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.id }} - {{ item.name }}
      </li>
    </ul>

    <hr />

    <input
      v-model="newName"
      placeholder="Nom du nouvel item"
    />
    <button @click="addItem">
      Ajouter
    </button>
  </div>
</template>