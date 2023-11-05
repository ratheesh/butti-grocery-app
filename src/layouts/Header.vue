<template>
  <nav class="navbar sticky-top navbar-expand-md bg-body-tertiary">
    <div class="container-fluid text-white px-0" style="background-color: #34494e">
      <router-link to="/" class="navbar-brand text-white">
        <div class="align-items-center">
          <mdicon name="basket" class="text-white color-success" :size="29" />
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
                  <mdicon class="text-white" name="home" :size="20" />Home
                </button>
              </router-link>
            </li>
            <li class="nav-item">
              <router-link :to="{ name: 'cart' }" class="nav-link">
                <button class="btn btn-sm btn-outline-primary">
                  <mdicon name="cart" class="text-white" :size="20" />
                  Cart
                  <span class="badge text-bg-warning">{{  cart.items.length }}</span>
                </button>
              </router-link>
            </li>
            <li v-if="!auth.authenticated" class="nav-link">
              <router-link :to="{ name: 'login' }" class="nav-link">
                <button class="btn btn-outline-success btn-sm">
                <mdicon class="text-white" name="login" :size="20" />
                  Login
                </button>
              </router-link>
            </li>
            <li v-else class="nav-link dropdown">
                  <a class="nav-link dropdown-toggle text-white p-0" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    <mdicon class="text-white" name="account" :size="20" />
                    {{ auth.user.username }}
                  </a>
              <ul class="dropdown-menu dropdown-menu-end">
                <router-link :to="{ name: 'profile' }" class="dropdown-item">
                  Profile
                </router-link>
                <li><span class="dropdown-item">Orders</span></li>
                <li><hr class="dropdown-divider"></li>
                <li class="nav-item mx-2" v-if="!auth.authenticated">
                  <router-link :to="{ name: 'login' }" class="dropdown-item">
                    Login
                  </router-link>
                </li>
                <li class="nav-item mx-2" v-else>
                  <span class="dropdown-item" @click="auth.logout">
                    Logout
                  </span>
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
import { RouterLink } from "vue-router";
import { useAuthStore } from "../stores/authstore";
import { useCartStore } from "../stores/cartstore";

const auth = useAuthStore();
const cart = useCartStore();
</script>

<style scoped></style>
