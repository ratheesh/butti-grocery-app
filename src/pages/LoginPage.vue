<template>
  <form-layout>
    <div class="container">
      <div class="row justify-content-center vh-auto">
        <div class="col-md-5">
          <div
            class="row col-md-12 col-lg-12 m-auto mt-3 px-0 d-inline-flex justify-content-center"
          >
            <div class="col-8 d-flex align-items-end justify-content-center">
              <mdicon name="basket" class="text-center text-primary mx-2" height="90" width="90" />
            </div>
          </div>
          <div class="card shadow-sm m-auto">
            <h3 class="text-center mt-3">Login</h3>
            <hr />
            <div class="card-body m-0 p-0">
              <form
                @submit.prevent="login"
                needs-validation
                novalidate
                :class="{ 'was-validated': wasValidated }"
              >
                <div class="row justify-content-center m-0 p-0">
                  <div class="col-md-10 m-0 p-0">
                    <div class="form-group mb-4">
                      <label for="username"
                        >User Name<span class="text-danger"><b>*</b></span></label
                      >
                      <div class="input-group">
                        <span class="input-group-text" id="username">
                          <mdicon name="account" :size="20" />
                        </span>
                        <input
                          type="text"
                          class="form-control rounded-end"
                          :class="{ 'form-control': true, 'is-invalid': errors.username }"
                          placeholder="username"
                          id="username"
                          v-model="username"
                          autofocus
                        />
                        <div class="invalid-feedback">
                          <span>Invalid User Name</span>
                        </div>
                      </div>
                    </div>
                    <div class="form-group mb-3">
                      <label for="password"
                        >Password<span class="text-danger"><b>*</b></span></label
                      >
                      <div class="input-group">
                        <span class="input-group-text" id="username">
                          <mdicon name="form-textbox-password" :size="20" />
                        </span>
                        <input
                          type="password"
                          class="form-control rounded-end"
                          v-model="password"
                          id="password"
                          :class="{ 'form-control': true, 'is-invalid': errors.password }"
                          placeholder="Enter password"
                        />
                        <div class="invalid-feedback">
                          <span>Invalid password</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <hr class="mt-1 mx-0" />
                <div class="mb-3 text-center">
                  <a
                    href="javascript:void(0)"
                    class="btn btn-sm btn-secondary d-inline-flex align-items-center mx-2"
                    @click="router.push('/')"
                  >
                    <span class="mx-1"><mdicon name="home" :size="18" /></span>
                    <span>Home</span>
                  </a>
                  <button
                    type="submit"
                    class="btn btn-sm btn-primary d-inline-flex align-items-center mx-2"
                  >
                    <span v-if="loading" class="spinner-border spinner-border-sm mx-1"></span>
                    <span v-if="!loading" class="mx-1"><mdicon name="login" :size="18" /></span>
                    <span>Login</span>
                  </button>
                  <span class="text-muted mx-2">Not a Member?</span>
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
  </form-layout>
</template>

<script setup>
import { ref, reactive } from 'vue'
// import axiosClient from '@/js/axios.js'
import router from '../router/index.js'
import { useAuthStore } from '@/stores/authstore.js'
import FormLayout from '@/layouts/FormLayout.vue'

const username = ref('')
const password = ref('')
let loading = ref(false)
const iserr = ref(false)
const errmsg = ref('')
const errors = reactive({
  username: false,
  password: false
})

const wasValidated = ref(false)

const auth = useAuthStore()

const login = async () => {
  wasValidated.value = false
  if (!username.value || !password.value) {
    console.log('Invalid username or password')
    iserr.value = true
    errmsg.value = 'Invalid username or password'
    errors.username = !username.value
    errors.password = !password.value
    return
  }
  wasValidated.value = true

  loading.value = true
  try {
    const res = await auth.login(username.value, password.value)
    if (res.status === 200) {
      console.log(`${auth.user.name} logged in as ${auth.user.role}`)

      if (router.currentRoute.value.query.redirect) {
        router.push(router.currentRoute.value.query.redirect)
        return
      }
      if (auth.user.role === 'admin') {
        router.push('/admin')
      } else if (auth.user.role === 'manager') {
        router.push('/manager')
      } else {
        router.push('/')
      }
    } else {
      console.log('Login Error')
      // console.log(res)
      wasValidated.value = false
      iserr.value = true
      errmsg.value = res.data
      errors.username = errmsg.value.includes('user')
      errors.password = errmsg.value.includes('password')
    }
  } catch (err) {
    console.log('Login Error')
    console.log(err)
    iserr.value = true
    errmsg.value = err.data
  } finally {
    loading.value = false
  }
}

const signup = () => {
  console.log('Signup')
  router.push('/signup')
}
</script>

<style scoped></style>
