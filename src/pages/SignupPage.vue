<template>
  <!-- <h1>signup view</h1> -->
  <basic-layout>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-6">
        <div class="card m-auto">
          <h2 class="text-center my-3">Signup</h2>
          <hr />
          <div class="card-body m-0 p-0">
            <form m-0 @submit.prevent="handleSignup">
              <div class="p-3">
                <div class="form-floating mb-3">
                  <input type="text" id="user" class="form-control" placeholder="Name" v-model="userdata.name" />
                  <label for="user">Name</label>
                </div>
                <div class="form-floating mb-3">
                  <input type="text" id="username" class="form-control" placeholder="User Name"
                    v-model="userdata.username" />
                  <label for="username">User Name</label>
                </div>
                <div class="form-floating mb-3">
                  <input type="text" id="email" class="form-control" placeholder="E-mail address"
                    v-model="userdata.email" />
                  <label for="email" class="form-label">E-Mail</label>
                </div>
                <div class="form-floating mb-3">
                  <select name="role" id="role" class="form-control" required="yes" v-model="userdata.role">
                    <option :value="options[0]" selected>user</option>
                    <option v-for='option in options' :value='option'>{{ option }}</option>
                  </select>
                  <label for="role" class="form-label">Role</label>
                </div>
                <div class="form-floating mb-3">
                  <input type="password" id="password" class="form-control" placeholder="Password"
                    v-model="userdata.password" />
                  <label for="password" class="form-label">Password</label>
                </div>
                <div class="form-floating mb-3">
                  <input type="password" id="password2" class="form-control" placeholder="Password"
                    v-model="userdata.password2" />
                  <label for="password2" class="form-label">Re-enter Password</label>
                </div>
              </div>
              <hr class="mt-1 mx-0" />
              <div class="mb-3 text-center">
                <button type="submit" class="btn btn-success">
                  <span v-if="loading" class="spinner-border spinner-border-sm"></span>
                  <span v-if="!loading"><mdicon name="account-plus" :size="25" /></span>
                  Signup
                </button>
                &nbsp;
                <span class="text-muted">Already a Member?</span>
                &nbsp;
                <a @click.prevent="handleLogin" href="#">Login</a>
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
  </basic-layout>
</template>

<script setup>
import { ref, reactive } from "vue";
import router from "@/router";
import { useAuthStore } from "@/stores/authstore.js";
import BasicLayout from "@/layouts/BasicLayout.vue"

const options=[ 'user', 'manager']

const userdata = reactive({
  name: "",
  username: "",
  email: "",
  role: "user",
  password: "",
  password2: "",
});

const loading = ref(false);
const iserr = ref(false);
const errmsg = ref("");

const auth = useAuthStore();

const handleSignup = async () => {
  console.log(userdata)
  if (userdata.name == '' || userdata.email=='' || userdata.role == '' || userdata.password=='' ||
  userdata.password2=='') {
    iserr.value = true;
    errmsg.value='Input data is not valid'
    return
  }  
  if (userdata.password != userdata.password2) {
    iserr.value=true;
    errmsg.value='Password does not match'
    userdata.password = userdata.password2=''
    return
  }

  try {
    loading.value = true;
    const res = await auth.signup(userdata);
    loading.value = false;
    if (res.status === 201)
     router.push("/");
    else {
      console.log("Signup Error");
      console.log(res);
      iserr.value = true;
      errmsg.value = res.data;
    }
  } catch (err) {
    loading.value=false
    console.log("Signup Error", err);
  }

  router.push("/signup");
};

const handleLogin = () => {
  console.log("Login");
  router.push("/login");
};
</script>

<style scoped></style>
