"use client";
import React from "react";
import z from "zod";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Button } from "@/components/ui/button";
import axios from "axios";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Loader } from "lucide-react";
import { AspectRatio } from "@/components/ui/aspect-ratio";
import Image from "next/image";

type ComponentProps = {};

// ~ ======= create the form schema  -->
const form_schema = z.object({
  hospital_id: z.string(),
  cough: z.coerce.boolean(),
  fever: z.coerce.boolean(),
  sore_throat: z.coerce.boolean(),
  shortness_of_breath: z.coerce.boolean(),
  head_ache: z.coerce.boolean(),
});

type PredictionResult = {
  prediction: number;
  message: string;
};

const PredictionForm: React.FC<ComponentProps> = ({}) => {
  // ~ ======= create states -->
  const [open, setOpen] = React.useState<boolean>(false);
  const [prediction_results, setPredictionResults] = React.useState<{
    svm_model: PredictionResult;
  } | null>(null);
  const [isLoading, setIsLoading] = React.useState(false);

  // ~ ======= instantiate form -->
  const form = useForm<z.infer<typeof form_schema>>({
    resolver: zodResolver(form_schema),
    defaultValues: {
      hospital_id: "",
      cough: false,
      fever: false,
      sore_throat: false,
      shortness_of_breath: false,
      head_ache: false,
    },
  });

  // ~ ======= submit handler -->
  const on_submit = async (form_data: z.infer<typeof form_schema>) => {
    setIsLoading(true);
    try {
      // ~ ======= make a request to our server -->
      // const rf_response = await axios.post(
      //   "http://localhost:8000/random_forest/predict",
      //   form_data,
      // );
      // const xgb_response = await axios.post(
      //   "http://localhost:8000/xgboost/predict",
      //   form_data,
      // );
      // const lr_response = await axios.post(
      //   "http://localhost:8000/logistic_regression/predict",
      //   form_data,
      // );
      // const nb_response = await axios.post(
      //   "http://localhost:8000/naive_bayes/predict",
      //   form_data,
      // );
      const svm_response = await axios.post(
        "http://localhost:8000/svm/predict",
        form_data,
      );

      setPredictionResults({
        svm_model: svm_response.data,
      });
      setOpen(true);
    } catch (error) {
      console.error("Error submitting form:", error);
      // Handle error (e.g., show an error message to the user)
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(on_submit)}
        className="w-full max-w-4xl grid grid-cols-4 gap-4 gap-y-6 rounded-lg shadow-xl pt-20 pb-8 border px-10"
      >
        {/* -- hospital id  */}
        <FormField
          control={form.control}
          render={({ field }) => (
            <FormItem className="col-span-2">
              <FormLabel>Hospital ID</FormLabel>
              <FormControl>
                <Input placeholder="Patient Hospital ID" {...field} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
          name="hospital_id"
        />

        {/* -- cough */}
        <FormField
          control={form.control}
          render={({ field }) => (
            <FormItem className="col-span-2">
              <FormLabel>Do you have cough</FormLabel>
              <FormControl>
                <Select
                  value={field.value ? "1" : "0"}
                  onValueChange={(value) =>
                    form.setValue("cough", value === "1")
                  }
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select an option" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="1">True</SelectItem>
                    <SelectItem value="0">False</SelectItem>
                  </SelectContent>
                </Select>
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
          name="cough"
        />

        {/* -- fever */}
        <FormField
          control={form.control}
          render={({ field }) => (
            <FormItem className="col-span-2">
              <FormLabel>Do you have a fever</FormLabel>
              <FormControl>
                <Select
                  value={field.value ? "1" : "0"}
                  onValueChange={(value) =>
                    form.setValue("fever", value === "1")
                  }
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select an option" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="1">True</SelectItem>
                    <SelectItem value="0">False</SelectItem>
                  </SelectContent>
                </Select>
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
          name="fever"
        />

        {/* -- sore throat */}
        <FormField
          control={form.control}
          render={({ field }) => (
            <FormItem className="col-span-2">
              <FormLabel>Do you have a fever</FormLabel>
              <FormControl>
                <Select
                  value={field.value ? "1" : "0"}
                  onValueChange={(value) =>
                    form.setValue("sore_throat", value === "1")
                  }
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select an option" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="1">True</SelectItem>
                    <SelectItem value="0">False</SelectItem>
                  </SelectContent>
                </Select>
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
          name="sore_throat"
        />

        {/* -- shortness of breath */}
        <FormField
          control={form.control}
          render={({ field }) => (
            <FormItem className="col-span-2">
              <FormLabel>Do yo feel short of breath sometimes</FormLabel>
              <FormControl>
                <Select
                  value={field.value ? "1" : "0"}
                  onValueChange={(value) =>
                    form.setValue("shortness_of_breath", value === "1")
                  }
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select an option" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="1">True</SelectItem>
                    <SelectItem value="0">False</SelectItem>
                  </SelectContent>
                </Select>
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
          name="shortness_of_breath"
        />

        {/* -- head ache */}
        <FormField
          control={form.control}
          render={({ field }) => (
            <FormItem className="col-span-2">
              <FormLabel>Do you have headaches</FormLabel>
              <FormControl>
                <Select
                  value={field.value ? "1" : "0"}
                  onValueChange={(value) =>
                    form.setValue("head_ache", value === "1")
                  }
                >
                  <SelectTrigger>
                    <SelectValue placeholder="Select an option" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="1">True</SelectItem>
                    <SelectItem value="0">False</SelectItem>
                  </SelectContent>
                </Select>
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
          name="head_ache"
        />
        {/* -- submit button */}
        <Button className="col-span-4 mt-8" disabled={isLoading}>
          {isLoading ? (
            <>
              <Loader className="mr-2 h-4 w-4 animate-spin" />
              Processing
            </>
          ) : (
            "Submit"
          )}
        </Button>

        <div className="col-span-4 flex items-center justify-center gap-5">
          <div className="w-16">
            <AspectRatio ratio={4 / 3}>
              <Image
                src="/images/tees.png"
                alt="NHIS-img"
                fill
                className="object-cover object-center"
              />
            </AspectRatio>
          </div>
          <span>Powered by Teesside University</span>
        </div>
        <ResultDialog
          open={open}
          hospital_id={form.getValues("hospital_id")}
          prediction_results={prediction_results}
          setOpen={setOpen}
        />
      </form>
    </Form>
  );
};

export default PredictionForm;

// ~ =============================================>
// ~ ======= Result dialog  -->
// ~ =============================================>
type DialogProps = {
  open: boolean;
  hospital_id: string;
  prediction_results: {
    svm_model: PredictionResult;
    // Add more models here as needed
  } | null;
  setOpen: React.Dispatch<React.SetStateAction<boolean>>;
};

const ResultDialog: React.FC<DialogProps> = ({
  open,
  setOpen,
  hospital_id,
  prediction_results,
}) => {
  const [expandedModel, setExpandedModel] = React.useState<string | null>(null);

  const renderModelResult = (modelName: string, result: PredictionResult) => (
    <div
      key={modelName}
      className="w-full mb-3 rounded-lg overflow-hidden border border-gray-200 transition-all duration-300 ease-in-out"
    >
      <div
        className="p-3 bg-white cursor-pointer hover:bg-gray-50"
        onClick={() =>
          setExpandedModel(expandedModel === modelName ? null : modelName)
        }
      >
        <div className="flex justify-between items-center">
          <h3 className="text-sm font-medium text-gray-700">
            {modelName.replace(/_/g, " ").toUpperCase()}
          </h3>
          <span
            className={`text-sm font-semibold ${
              result.prediction === 0 ? "text-green-600" : "text-red-600"
            }`}
          >
            {result.prediction === 0 ? "Negative" : "Positive"}
          </span>
        </div>
        {expandedModel === modelName && (
          <p className="mt-2 text-xs text-gray-600">{result.message}</p>
        )}
      </div>
    </div>
  );

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle className="text-xl font-bold text-center">
            Prediction Results
          </DialogTitle>
          <DialogDescription className="text-center text-sm text-gray-600">
            Case for {hospital_id} has been analyzed using multiple models.
          </DialogDescription>
        </DialogHeader>
        <div className="w-full flex flex-col py-4">
          {prediction_results &&
            Object.entries(prediction_results).map(([modelName, result]) =>
              renderModelResult(modelName, result),
            )}
        </div>
        <div className="mt-2 text-center text-xs text-gray-500">
          Click on each model to view detailed results.
        </div>
        <Button onClick={() => setOpen(false)} className="mt-4 w-full">
          Make new prediction
        </Button>
      </DialogContent>
    </Dialog>
  );
};
