import { NextResponse } from 'next/server';
import { db, storage } from '@/lib/firebase-admin';

export async function POST(request: Request) {
  try {
    const data = await request.formData();
    const image = data.get('image') as File;
    const disease = data.get('disease') as string;
    const latitude = parseFloat(data.get('latitude') as string);
    const longitude = parseFloat(data.get('longitude') as string);

    if (!image || !disease || !latitude || !longitude) {
      return NextResponse.json(
        { error: 'Missing required fields' },
        { status: 400 }
      );
    }

    // Upload image to Firebase Storage
    const buffer = await image.arrayBuffer();
    const filename = `plants/${Date.now()}_${image.name}`;
    const file = storage.bucket().file(filename);
    await file.save(Buffer.from(buffer));
    await file.makePublic();

    const imageUrl = `https://storage.googleapis.com/${process.env.FIREBASE_STORAGE_BUCKET}/${filename}`;

    // Save data to Firestore
    const plantRef = await db.collection('plants').add({
      imageUrl,
      disease,
      latitude,
      longitude,
      timestamp: new Date().toISOString(),
    });

    return NextResponse.json({
      id: plantRef.id,
      message: 'Data uploaded successfully',
    });
  } catch (error) {
    console.error('Error uploading data:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}