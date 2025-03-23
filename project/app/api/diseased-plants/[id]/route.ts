import { NextResponse } from 'next/server';
import { db } from '@/lib/firebase-admin';

export async function GET(
  request: Request,
  { params }: { params: { id: string } }
) {
  try {
    const plantDoc = await db.collection('plants').doc(params.id).get();

    if (!plantDoc.exists) {
      return NextResponse.json(
        { error: 'Plant not found' },
        { status: 404 }
      );
    }

    return NextResponse.json({
      id: plantDoc.id,
      ...plantDoc.data()
    });
  } catch (error) {
    console.error('Error fetching plant:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}