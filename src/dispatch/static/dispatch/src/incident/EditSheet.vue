<template>
  <ValidationObserver v-slot="{ invalid, validated }">
    <v-navigation-drawer v-model="showEditSheet" app clipped right width="800">
      <template v-slot:prepend>
        <v-list-item two-line>
          <v-list-item-content>
            <v-list-item-title class="title">{{ name }}</v-list-item-title>
            <v-list-item-subtitle>Reported - {{ reported_at | formatDate }}</v-list-item-subtitle>
          </v-list-item-content>
          <v-btn
            icon
            color="primary"
            :loading="loading"
            :disabled="invalid || !validated"
            @click="save()"
          >
            <v-icon>save</v-icon>
          </v-btn>
          <v-btn icon color="secondary" @click="closeEditSheet">
            <v-icon>close</v-icon>
          </v-btn>
        </v-list-item>
      </template>
      <v-tabs fixed-tabs v-model="tab">
        <v-tab key="details">Details</v-tab>
        <v-tab key="resources">Resources</v-tab>
        <v-tab key="participants">Participants</v-tab>
        <v-tab key="timeline">Timeline</v-tab>
      </v-tabs>
      <v-tabs-items v-model="tab">
        <incident-details-tab />
        <incident-resources-tab />
        <incident-participants-tab />
      </v-tabs-items>
    </v-navigation-drawer>
  </ValidationObserver>
</template>

<script>
import { mapFields } from "vuex-map-fields"
import { mapActions } from "vuex"
import { ValidationObserver } from "vee-validate"

import IncidentDetailsTab from "@/incident/DetailsTab.vue"
import IncidentResourcesTab from "@/incident/ResourcesTab.vue"
import IncidentParticipantsTab from "@/incident/ParticipantsTab.vue"

export default {
  name: "IncidentEditSheet",

  components: {
    ValidationObserver,
    IncidentDetailsTab,
    IncidentResourcesTab,
    IncidentParticipantsTab
  },

  data() {
    return {
      tab: null
    }
  },

  computed: {
    ...mapFields("incident", [
      "selected.id",
      "selected.name",
      "selected.reported_at",
      "selected.loading",
      "dialogs.showEditSheet"
    ])
  },

  methods: {
    ...mapActions("incident", ["save", "closeEditSheet"])
  }
}
</script>
