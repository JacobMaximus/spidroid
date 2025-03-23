import { db } from "@/lib/firebase-admin";
import { NextResponse } from "next/server";

export async function GET() {
  try {
    const testRef = await db.collection("test").add({ message: "Firebase is working!" });
    return NextResponse.json({ success: true, id: testRef.id });
  } catch (error) {
    // return NextResponse.json({ success: false, error: error.message });
  }
}
