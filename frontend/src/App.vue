<script setup lang="ts">
import { ref } from 'vue'

const API_URL=import.meta.env.VITE_API_URL

const ready = ref(false)
const downloadAnchor = ref<undefined | HTMLAnchorElement>()

const converting = ref(false)
const statusText = ref('Converting...')
const ytUrl = ref<undefined | string>()

const handleSubmit = async (type: string) => {
  if (!(ytUrl.value && downloadAnchor.value)) return

  const params = new URLSearchParams({ url: ytUrl.value })

  let path: string | undefined

  if (type == 'audio') {
    path = 'download-audio'
  } else if (type == 'video') {
    path = 'download-video'
  } else {
    return
  }

  converting.value = true
  ready.value = false

  const res = await fetch(`${API_URL}/${path}/?${params.toString()}`)

  let filename = res.headers.get('Content-Disposition')

  if (filename) {
    filename = decodeURIComponent(filename)
    filename = filename.replace("attachment; filename*=utf-8''", '')
  }

  const blob = await res.blob()
  const virtualUrl = URL.createObjectURL(blob)

  downloadAnchor.value.href = virtualUrl
  downloadAnchor.value.download = filename || 'no-name'

  converting.value = false
  ready.value = true
}
</script>

<template>
  <main class="flex flex-col h-screen justify-center items-center">
    <p>URL:</p>
    <input class="border p-2 mb-4" v-model="ytUrl" />
    <p v-if="converting">{{ statusText }}</p>
    <a
      :class="`mb-2 cursor-pointer bg-[#2abd71] w-30 rounded p-4 text-center ${!ready && 'hidden'}`"
      ref="downloadAnchor"
      >Download</a
    >

    <div class="space-x-4">
      <button class="cursor-pointer bg-[#2abd71] w-30 rounded p-4 text-center" @click="handleSubmit('audio')">
        Extract Audio
      </button>

      <button class="cursor-pointer bg-[#2abd71] w-30 rounded p-4 text-center" @click="handleSubmit('video')">
        Extract Video
      </button>
    </div>
  </main>
</template>
