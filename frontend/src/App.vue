<template>
  <div class="container">
    <h1>Multiplication</h1>
    <MultiplicationForm />
  </div>
</template>

<script>
import MultiplicationForm from './components/MultiplicationForm.vue'

export default {
  name: 'App',
  components: {
    MultiplicationForm
  }
}
</script>

<style>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}
</style>