<template>
  <div class="greetings">
    <h1 class="green">Get IP.</h1>
    <h3>Let's you access your LoraWAN's gateway IP address.</h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 700;
  font-size: 3rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1rem;
  font-weight: 500;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
