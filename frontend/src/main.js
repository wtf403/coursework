import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router';
import store from './store';
import components from '@/components/UI';
import directives from '@/directives';
import VueSvgInlinePlugin from 'vue-svg-inline-plugin';
import vuetify from '@/plugins/vuetify';
const app = createApp(App);
components.forEach((component) => {
  app.component(component.name, component);
});
directives.forEach((directive) => {
  app.directive(directive.name, directive);
});


app.use(router).use(store).use(vuetify).use(VueSvgInlinePlugin).mount('#app');
