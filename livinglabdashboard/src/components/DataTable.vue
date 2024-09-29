<template>
  <v-card>
    <v-card-title>Datentabelle</v-card-title>
    <v-card-text>
      <v-data-table
        :headers="headers"
        :items="items"
        :items-per-page="500"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-text-field
            v-model="search"
            label="Suche"
            class="mx-4"
          ></v-text-field>
        </template>
      </v-data-table>
    </v-card-text>
  </v-card>
</template>

<script>
import apiClient from "../plugins/axios";

export default {
  name: "DataTable",
  data() {
    return {
      headers: [
        { text: "ID", value: "id" },
        { text: "Name", value: "name" },
        { text: "Wert", value: "value" },
        // Weitere Spalten je nach Datenbanktabellen
      ],
      items: [],
      search: "",
    };
  },
  async created() {
    await this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await apiClient.get("/data", {
          params: { limit: 500 },
        });
        this.items = response.data;
      } catch (error) {
        console.error("Fehler beim Abrufen der Daten:", error);
      }
    },
  },
};
</script>

<style scoped>
/* Optional: Styling */
</style>
