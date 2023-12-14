<template>
  <nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-body-tertiary p-0">
    <div class="container-fluid text-white m-0 p-0" style="background-color: #2f3640">
      <router-link to="/" class="navbar-brand text-white">
        <div class="d-flex align-items-base">
          <mdicon name="basket" class="text-warning color-success mx-3" :size="36" />
          <span class="fs-4">Butti</span>
        </div>
      </router-link>
      <div>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <form class="d-flex" role="search" @submit.prevent="handleSearch">
            <input
              class="form-control-sm me-1 border-2"
              type="search"
              placeholder="Search"
              v-model="query"
              aria-label="Search"
            />
            <button class="btn btn-sm btn-outline-success" type="submit">
              <mdicon name="magnify" :size="20" />
            </button>
          </form>
          <ul class="navbar-nav me-auto mb-3 mb-lg-0 my-auto align-items-center">
            <li class="nav-item">
              <router-link :to="{ name: 'home' }" class="nav-link">
                <button class="btn btn-sm btn-outline-light">
                  <mdicon name="home" :size="20" />Home
                </button>
              </router-link>
            </li>
            <li v-if="user && user.role == 'user'" class="nav-item">
              <router-link :to="{ name: 'cart' }" class="nav-link">
                <button class="btn btn-sm btn-outline-rosy-brown">
                  <mdicon name="cart" :size="20" />
                  Cart
                  <span class="badge text-bg-warning">{{ cart.items.length }}</span>
                </button>
              </router-link>
            </li>
            <li v-if="!authenticated" class="nav-link">
              <router-link :to="{ name: 'login' }" class="nav-link">
                <button class="btn btn-outline-info btn-sm">
                  <mdicon name="login" :size="20" />
                  Login
                </button>
              </router-link>
            </li>
            <li v-else class="nav-link dropdown">
              <a
                class="nav-link dropdown-toggle text-white p-0"
                href="javascript:void(0)"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                <!-- <mdicon name="account" :size="20" /> -->
                <img
                  :src="`data:image/png;base64,${user.image}`"
                  alt="avatar"
                  class="rounded-circle"
                  width="28"
                  height="28"
                  style="border: 50%"
                />
                <span class="ms-2 fs-6">{{ user.name }}</span>
              </a>
              <ul class="dropdown-menu dropdown-menu-end">
                <a class="dropdown-item" href="javascript:void(0)">
                  <router-link :to="{ name: 'profile' }" class="dropdown-item">
                    <mdicon name="account" :size="20" />
                    Profile
                  </router-link>
                </a>
                <li v-if="user.role == 'user'">
                  <a class="dropdown-item" href="javascript:void(0)" style="text-decoration-none">
                    <router-link :to="{ name: 'orders' }" class="dropdown-item">
                      <svg
                        fill="#000000"
                        xmlns="http://www.w3.org/2000/svg"
                        width="20"
                        height="20"
                        viewBox="0 0 100 100"
                        xml:space="preserve"
                      >
                        <g>
                          <g>
                            <path
                              d="M78.8,62.1l-3.6-1.7c-0.5-0.3-1.2-0.3-1.7,0L52,70.6c-1.2,0.6-2.7,0.6-3.9,0L26.5,60.4
                            c-0.5-0.3-1.2-0.3-1.7,0l-3.6,1.7c-1.6,0.8-1.6,2.9,0,3.7L48,78.5c1.2,0.6,2.7,0.6,3.9,0l26.8-12.7C80.4,65,80.4,62.8,78.8,62.1z"
                            />
                          </g>
                          <g>
                            <path
                              d="M78.8,48.1l-3.7-1.7c-0.5-0.3-1.2-0.3-1.7,0L52,56.6c-1.2,0.6-2.7,0.6-3.9,0L26.6,46.4
                            c-0.5-0.3-1.2-0.3-1.7,0l-3.7,1.7c-1.6,0.8-1.6,2.9,0,3.7L48,64.6c1.2,0.6,2.7,0.6,3.9,0l26.8-12.7C80.4,51.1,80.4,48.9,78.8,48.1
                            z"
                            />
                          </g>
                          <g>
                            <path
                              d="M21.2,37.8l26.8,12.7c1.2,0.6,2.7,0.6,3.9,0l26.8-12.7c1.6-0.8,1.6-2.9,0-3.7L51.9,21.4
                            c-1.2-0.6-2.7-0.6-3.9,0L21.2,34.2C19.6,34.9,19.6,37.1,21.2,37.8z"
                            />
                          </g>
                        </g>
                      </svg>
                      Orders
                    </router-link>
                  </a>
                </li>
                <li><hr class="dropdown-divider" /></li>
                <li class="nav-item mx-2" v-if="!authenticated">
                  <router-link :to="{ name: 'login' }" class="dropdown-item"> Login </router-link>
                </li>
                <li class="nav-item mx-2" v-else>
                  <a class="dropdown-item" href="javascript:void(0)">
                    <span @click="auth.logout">
                      <mdicon name="power" class="fw-bolder text-danger" :size="20" />
                      Logout
                    </span>
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import { useAuthStore } from '../stores/authstore'
import { useCartStore } from '../stores/cartstore'
import { storeToRefs } from 'pinia'
import router from '../router/index.js'
// import { onMounted } from 'vue';

const query = ref('')
const auth = useAuthStore()
const cart = useCartStore()

const { user, authenticated } = storeToRefs(auth)

const handleSearch = () => {
  if (query.value) {
    console.log('searching for', query.value)
    router.push({ name: 'search', params: { query: query.value } })
  }
}
</script>

<style scoped></style>
