import axios from 'axios'

const axiosClient = axios.create({
  baseURL: 'http://localhost:5000',
  withcredentials: true,
  headers: {
    'Content-Type': 'application/json',
    common: {
      Authorization: `Bearer ${localStorage.getItem('access_token')}`
    }
  }
})

export default axiosClient
