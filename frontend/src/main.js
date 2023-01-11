import { createApp } from 'vue';
import App from './App.vue';
import router from './router/router';
import store from './store';
import components from '@/components/UI';
import directives from '@/directives';
import VueSvgInlinePlugin from 'vue-svg-inline-plugin';
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

const app = createApp(App);
components.forEach((component) => {
  app.component(component.name, component);
});
directives.forEach((directive) => {
  app.directive(directive.name, directive);
});


app.use(router).use(store).use(Antd).use(VueSvgInlinePlugin).mount('#app');
