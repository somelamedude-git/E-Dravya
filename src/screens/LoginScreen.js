import React, { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Pressable,
  StyleSheet,
} from 'react-native';

const LoginScreen = ({ navigation }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  const handleLogin = () => {
    if (email === 'user@example.com' && password === 'password123') {
      alert('Login successful!');
      navigation.navigate('Home');
    } else {
      alert('Invalid email or password');
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.card}>
        <Text style={styles.title}>Log In</Text>
        <TextInput
          style={styles.input}
          placeholder="Email"
          placeholderTextColor="#9CA3AF"
          value={email}
          onChangeText={setEmail}
          autoCapitalize="none"
        />
        <View style={styles.passwordContainer}>
          <TextInput
            style={styles.inputPassword}
            placeholder="Password"
            placeholderTextColor="#9CA3AF"
            value={password}
            onChangeText={setPassword}
            secureTextEntry={!showPassword}
            autoCapitalize="none"
          />
          <Pressable
            onPress={() => setShowPassword(!showPassword)}
            style={styles.eyeBtn}
          >
            <Text style={{ color: '#6EE7B7', fontWeight: 'bold' }}>
              {showPassword ? 'Hide' : 'Show'}
            </Text>
          </Pressable>
        </View>
        <TouchableOpacity style={styles.button} onPress={handleLogin}>
          <Text style={styles.buttonText}>Sign In</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#232946', // main dark blue
    justifyContent: 'center',
    alignItems: 'center',
  },
  card: {
    width: '91%',
    backgroundColor: '#20202c', // panel card color
    borderRadius: 21,
    padding: 32,
    shadowColor: '#000',
    shadowOpacity: 0.15,
    shadowOffset: { width: 0, height: 12 },
    shadowRadius: 21,
    elevation: 10,
    alignItems: 'center',
  },
  title: {
    color: '#6EE7B7', // green highlight
    fontSize: 27,
    fontWeight: 'bold',
    marginBottom: 38,
    letterSpacing: 1,
  },
  input: {
    width: '100%',
    padding: 13,
    marginVertical: 9,
    borderRadius: 9,
    backgroundColor: '#2D3250',
    color: '#fff',
    fontSize: 16,
    borderWidth: 1,
    borderColor: '#363858',
  },
  passwordContainer: {
    width: '100%',
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#2D3250',
    borderRadius: 9,
    marginVertical: 9,
    borderWidth: 1,
    borderColor: '#363858',
  },
  inputPassword: {
    flex: 1,
    padding: 13,
    color: '#fff',
    fontSize: 16,
  },
  eyeBtn: {
    paddingHorizontal: 12,
    paddingVertical: 9,
  },
  button: {
    marginTop: 29,
    width: '100%',
    backgroundColor: '#38BDF8', // blue/green action btn
    borderRadius: 9,
    paddingVertical: 15,
    alignItems: 'center',
    shadowColor: '#38BDF8',
    shadowOpacity: 0.2,
    shadowOffset: { width: 0, height: 8 },
    elevation: 3,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 17,
    letterSpacing: 1,
  },
});

export default LoginScreen;
