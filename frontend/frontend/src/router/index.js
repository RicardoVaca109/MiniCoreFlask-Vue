import Vue from "vue";
import VueRouter from "vue-router";
import SharkComponent from "@/components/SharkComponent.vue";
import CarsComponent from "@/components/CarsComponent.vue";
Vue.use(VueRouter);
const routes = [
  {
    path: "/shark",
    name: "SharkComponent",
    component: SharkComponent,
  },
  {
    path: "/cars",
    name: "CarsComponent",
    component: CarsComponent,
  },
];
const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});
export default router;
