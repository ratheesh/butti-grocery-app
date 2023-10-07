<template>
  <BasicLayout>
  <div class="container">
    <div class="row justify-content-md-center vh-auto">
      <pre>{{ username }}</pre>
      <pre>{{ password }}</pre>
      <div class="col-md-5">
        <div class="card m-auto">
          <h2 class="text-center my-3">Login</h2>
          <hr />
          <div class="card-body m-0 p-0">
            <form @submit.prevent="login">
              <div class="mb-3 px-3">
                <label for="username" class="form-label">User Name</label>
                <input
                  type="text"
                  v-model="username"
                  id="username"
                  class="form-control"
                  placeholder="User Name"
                />
              </div>
              <div class="mb-3 px-3">
                <label for="password" class="form-label">Password</label>
                <input
                  type="password"
                  v-model="password"
                  id="password"
                  class="form-control"
                  placeholder="Enter password"
                />
              </div>
              <hr class="mt-3 mx-0" />
              <div class="mb-3 text-center">
                <button type="submit" class="btn btn-success btn">
                  <span v-if="loading" class="spinner-border spinner-border-sm"></span>
                  <span v-if="!loading"><mdicon name="login" :size="18" /></span
                  >&nbsp;Login
                </button>
                &nbsp;
                <span class="text-muted">Not a Member?</span>
                &nbsp;
                <a @click.prevent="signup" href="">Signup</a>
              </div>
            </form>
            <div class="alert alert-danger mx-3 text-center" role="alert" v-if="iserr">
              {{ errmsg }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  </BasicLayout>
</template>

<script setup>
import { ref } from "vue";
import router from "@/router";
import { useAuthStore } from "@/stores/authstore.js";
import BasicLayout from "@/layouts/BasicLayout.vue"

const username = ref("");
const password = ref("");
let loading = ref(false);
const iserr = ref(false);
const errmsg = ref("");

const auth = useAuthStore();

const login = async () => {
  loading.value = true;
  try {
    const res = await auth.login(username.value, password.value);
    loading.value = false;
    if (res.status === 200)
     router.push("/");
    else {
      console.log("Login Page Error");
      console.log(res);
      iserr.value = true;
      errmsg.value = res.data;
    }
  } catch (err) {
    loading.value = false;
  }
};

const signup = () => {
  console.log("Signup");
  router.push("/signup");
};
</script>

<style scoped></style>
