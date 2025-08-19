# Firebase Setup for Otterful Otter Bros Leaderboard

## 🚀 Quick Setup Guide

### 1. Create Firebase Project
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project"
3. Name it "otterful-otter-bros" (or your preferred name)
4. Enable Google Analytics (optional)
5. Click "Create project"

### 2. Enable Firestore Database
1. In your Firebase project, go to "Firestore Database"
2. Click "Create database"
3. Choose "Start in test mode" (for development)
4. Select a location close to your users
5. Click "Done"

### 3. Get Your Configuration
1. Click the gear icon ⚙️ next to "Project Overview"
2. Select "Project settings"
3. Scroll down to "Your apps" section
4. Click the web icon (</>)
5. Register your app with a nickname (e.g., "Otterful Otter Bros")
6. Copy the configuration object

### 4. Update Configuration
Replace the placeholder config in `firebase-config.js` with your actual Firebase config:

```javascript
const firebaseConfig = {
    apiKey: "your-actual-api-key",
    authDomain: "your-project-id.firebaseapp.com",
    projectId: "your-project-id",
    storageBucket: "your-project-id.appspot.com",
    messagingSenderId: "your-sender-id",
    appId: "your-app-id"
};
```

### 5. Security Rules (Optional)
For production, update Firestore security rules:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Allow read access to all players collection
    match /players/{playerId} {
      allow read: if true;
      allow write: if request.auth != null && request.auth.uid == playerId;
    }
  }
}
```

## 📊 Database Schema

### Players Collection
```javascript
{
  walletAddress: "0x16e315e37cdeda413d22a6899fff67a4b001d91b",
  totalStaked: 4,
  totalEarned: 1250,
  stakingStartTime: "2024-01-15T10:30:00Z",
  stakedNFTs: [
    { tokenId: 66, stakedAt: "2024-01-15T10:30:00Z", multiplier: 1.0 },
    { tokenId: 373, stakedAt: "2024-01-15T10:30:00Z", multiplier: 3.49 }
  ],
  lastUpdated: "2024-01-15T12:45:00Z",
  totalMultiplier: 4.49
}
```

## 🔧 Features Implemented

### ✅ Leaderboard System
- **Top Earners** - Highest $FISH earned
- **Most Staked** - Most NFTs staked
- **Best Multipliers** - Highest multiplier collections

### ✅ Global Statistics
- Total players
- Total NFTs staked
- Total $FISH earned
- Average staking time

### ✅ Real-time Updates
- Automatic database updates when staking
- Real-time leaderboard refresh
- Player stats tracking

## 🎯 API Endpoints

The system automatically handles these operations:

- `GET /players` - Fetch all players
- `GET /players/{walletAddress}` - Get specific player
- `POST /players/{walletAddress}` - Update player stats
- `GET /leaderboard` - Get sorted leaderboard

## 🚨 Important Notes

1. **Free Tier Limits**: Firebase has generous free limits:
   - 50,000 reads/day
   - 20,000 writes/day
   - 1GB storage

2. **Security**: For production, implement proper authentication and security rules

3. **Backup**: Consider regular database backups for important data

4. **Monitoring**: Use Firebase Analytics to track usage

## 🐛 Troubleshooting

### Common Issues:
1. **"Firebase not initialized"** - Check your config is correct
2. **"Permission denied"** - Update Firestore security rules
3. **"Network error"** - Check internet connection and Firebase status

### Debug Mode:
Open browser console and look for:
- ✅ Firebase connection success
- 📊 Database update confirmations
- ❌ Error messages

## 📈 Next Steps

1. **Deploy to Production**: Update security rules
2. **Add Authentication**: Implement user login system
3. **Analytics**: Add Firebase Analytics for insights
4. **Backup Strategy**: Set up automated backups
5. **Monitoring**: Add error tracking and performance monitoring
