<template>
  <div class="form-container">
    <div class="input-group">
      <label for="value1">Value 1:</label>
      <input 
        type="number" 
        id="value1" 
        v-model="value1" 
        placeholder="Enter first value"
      >
    </div>
    
    <div class="input-group">
      <label for="value2">Value 2:</label>
      <input 
        type="number" 
        id="value2" 
        v-model="value2" 
        placeholder="Enter second value"
      >
    </div>

    <button @click="calculate" class="calculate-btn">Calculate</button>

    <div class="result" :class="{ error: isError }">
      {{ result }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MultiplicationForm',
  data() {
    return {
      value1: '',
      value2: '',
      result: '',
      isError: false
    }
  },
  methods: {
    async calculate() {
      try {
        // Validate input before sending
        if (!this.value1 || !this.value2) {
          this.result = 'Error: Please enter both values';
          this.isError = true;
          return;
        }

        const response = await fetch('http://localhost:8000/api/multiply/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            value1: parseFloat(this.value1),
            value2: parseFloat(this.value2)
          })
        });

        const data = await response.json();
        console.log('Response:', data); // Add this for debugging
        
        if (response.ok) {
          this.result = `Result: ${data.result}`;
          this.isError = false;
        } else {
          this.result = `Error: ${data.detail || 'Please enter valid numbers'}`;
          this.isError = true;
        }
      } catch (error) {
        console.error('Error:', error); // Add this for debugging
        this.result = 'Error: Could not connect to the server. Is the backend running?';
        this.isError = true;
      }
    }
  }
}
</script>