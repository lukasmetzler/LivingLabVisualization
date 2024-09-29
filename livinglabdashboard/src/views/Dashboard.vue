<template>
  <v-container>
    <v-row>
      <v-col>
        <h1>Willkommen zum Dashboard</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" md="6">
        <DataTable />
      </v-col>
      <v-col cols="12" md="6">
        <DataTable />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import DataTable from "../components/DataTable.vue";
import DataTable from "../components/DataTable.vue";
export default {
  name: "Dashboard",
  components: {
    DataTable,
  },
};
</script>

<style scoped>
/* Optional: Styling */
</style>
