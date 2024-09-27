<template>
  <v-container>
    <h1>Welcome, {{ $auth.user.username }}!</h1>
  </v-container>
</template>

<script>
export default {
  middleware: "auth",
};
</script>
