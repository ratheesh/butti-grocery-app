<template>
  <nav class="navbar sticky-top navbar-expand-md bg-body-tertiary">
    <div class="container-fluid text-white" style="background-color: #34494e">
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
              class="form-control me-3 border-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
            />
            <button class="btn btn-outline-success" type="submit">
              <mdicon name="magnify" :size="29" />
            </button>
          </form>
          <ul class="navbar-nav me-auto mb-3 mb-lg-0">
            <li class="nav-item mx-2">
              <router-link :to="{ name: 'home' }" class="nav-link">
                <mdicon class="text-white" name="home" :size="29" />
              </router-link>
            </li>
            <li class="nav-item mx-2">
              <router-link :to="{ name: 'cart' }" class="nav-link">
                <mdicon name="cart" class="text-white" :size="29" />
                <span class="badge text-bg-warning">{{  cart.items.length }}</span>
              </router-link>
            </li>
            <li class="nav-item mx-2 dropdown">
              <a class="nav-link dropdown-toggle text-white" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <mdicon class="text-white" name="account" :size="29" />
              </a>
              <ul class="dropdown-menu dropdown-menu-end">
                <router-link :to="{ name: 'profile' }" class="dropdown-item">
                  Profile
                </router-link>
                <li><span class="dropdown-item">Orders</span></li>
                <li><hr class="dropdown-divider"></li>
                <li class="nav-item mx-2" v-if="!auth.authenticated">
                  <router-link :to="{ name: 'login' }" class="nav-link">
                    Login
                  </router-link>
                </li>
                <li class="nav-item mx-2" v-else>
                  <span class="nav-link" @click="auth.logout">
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
