<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>LivingLab</v-toolbar-title>
      <v-spacer></v-spacer>
      <div v-if="$auth.loggedIn">
        <v-btn text @click="logout">Logout</v-btn>
      </div>
    </v-app-bar>
    <v-content>
      <Nuxt />
    </v-content>
  </v-app>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$auth.logout();
    },
  },
};
</script>
