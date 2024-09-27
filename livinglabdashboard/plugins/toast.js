// plugins/toast.js

import Vue from "vue";
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

// Optionen können angepasst werden
const options = {
  // Position: 'top-right', 'top-center', 'top-left', 'bottom-right', 'bottom-center', 'bottom-left'
  position: "top-right",
  timeout: 5000,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
  showCloseButtonOnHover: false,
  hideProgressBar: false,
  closeButton: "button",
  icon: true,
  rtl: false,
};

Vue.use(Toast, options);
