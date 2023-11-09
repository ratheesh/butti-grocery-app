import axios from 'axios'

const axiosClient = axios.create({
  baseURL: 'http://localhost:5000',
  withcredentials: true,
  headers: {
    common: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('access_token')}`
    }
  }
})

export default axiosClient
