import '@mdi/font/css/materialdesignicons.css';
import 'vuetify/styles';
// Vuetify
import { createVuetify } from 'vuetify';
import * as Vcomponents from 'vuetify/components';
import * as Vdirectives from 'vuetify/directives';


const vuetify = createVuetify({
  Vcomponents,
  Vdirectives,
  ssr: true,
});
