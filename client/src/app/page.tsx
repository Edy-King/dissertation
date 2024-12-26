import PredictionForm from "@/components/prediction_form";
import { AspectRatio } from "@/components/ui/aspect-ratio";
import Image from "next/image";

export default function Home() {
  return (
    <div className="min-h-screen bg-neutral-100 flex flex-col">
      <header className="w-full p-10 bg-white shadow-sm flex items-center gap-10">
        <div className="max-w-7xl ">
          <h1 className="text-2xl font-bold text-gray-800">
            COVID-19 Risk Assessment
          </h1>
          <p className="mt-2 text-gray-600">
            Predict your risk using our advanced machine learning model
          </p>
        </div>
      </header>

      <main className="flex-grow flex items-center justify-center p-6">
        <div className="w-full max-w-4xl bg-white rounded-xl shadow-xl overflow-hidden">
          <div className="p-4 bg-indigo-500 text-white">
            <h2 className="text-xl font-semibold no-underline border-0">
              Symptom Checker
            </h2>
          </div>
          <PredictionForm />
        </div>
      </main>
    </div>
  );
}
