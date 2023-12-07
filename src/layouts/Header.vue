<template>
  <nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-body-tertiary p-0">
    <div class="container-fluid text-white m-0 p-0" style="background-color: #2f3640">
      <router-link to="/" class="navbar-brand text-white">
        <div class="d-flex align-items-center">
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
          <form class="d-flex" role="search">
            <input
              class="form-control-sm me-1 border-2"
              type="search"
              placeholder="Search"
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
            <li class="nav-item">
              <router-link :to="{ name: 'cart' }" class="nav-link">
                <button class="btn btn-sm btn-outline-rosy-brown">
                  <mdicon name="cart" :size="20" />
                  Cart
                  <span class="badge text-bg-warning">{{ cart.items.length }}</span>
                </button>
              </router-link>
            </li>
            <li v-if="!auth.authenticated" class="nav-link">
              <router-link :to="{ name: 'login' }" class="nav-link">
                <button class="btn btn-outline-info btn-sm">
                  <!-- <mdicon class="text-white" name="login" :size="20" /> -->
                  <svg
                    width="20px"
                    height="20px"
                    viewBox="0 0 24 24"
                    fill="#000"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      fill-rule="evenodd"
                      clip-rule="evenodd"
                      d="M8 6C8 3.79086 9.79086 2 12 2H17.5C19.9853 2 22 4.01472 22 6.5V17.5C22 19.9853 19.9853 22 17.5 22H12C9.79086 22 8 20.2091 8 18V17C8 16.4477 8.44772 16 9 16C9.55228 16 10 16.4477 10 17V18C10 19.1046 10.8954 20 12 20H17.5C18.8807 20 20 18.8807 20 17.5V6.5C20 5.11929 18.8807 4 17.5 4H12C10.8954 4 10 4.89543 10 6V7C10 7.55228 9.55228 8 9 8C8.44772 8 8 7.55228 8 7V6ZM12.2929 8.29289C12.6834 7.90237 13.3166 7.90237 13.7071 8.29289L16.7071 11.2929C17.0976 11.6834 17.0976 12.3166 16.7071 12.7071L13.7071 15.7071C13.3166 16.0976 12.6834 16.0976 12.2929 15.7071C11.9024 15.3166 11.9024 14.6834 12.2929 14.2929L13.5858 13L5 13C4.44772 13 4 12.5523 4 12C4 11.4477 4.44772 11 5 11L13.5858 11L12.2929 9.70711C11.9024 9.31658 11.9024 8.68342 12.2929 8.29289Z"
                      fill="#0F1729"
                    />
                  </svg>
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
                <mdicon name="account" :size="20" />
                {{ auth.user.username }}
              </a>
              <ul class="dropdown-menu dropdown-menu-end">
                <a class="dropdown-item" href="javascript:void(0)">
                  <router-link :to="{ name: 'profile' }" class="dropdown-item">
                    <mdicon name="account" :size="20" />
                    Profile
                  </router-link>
                </a>
                <li>
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
                <li class="nav-item mx-2" v-if="!auth.authenticated">
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
import { RouterLink } from 'vue-router'
import { useAuthStore } from '../stores/authstore'
import { useCartStore } from '../stores/cartstore'

const auth = useAuthStore()
const cart = useCartStore()
</script>

<style scoped></style>
