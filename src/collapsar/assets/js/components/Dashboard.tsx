import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

export function Dashboard() {
  return (
    <div>
      <div className="container">
        <div className="mb-5">
          <h1 className="text-2xl">Welcome to Collapsar 🚀</h1>
          <p className="text-secondary-foreground">
            This is the first to create great things. If you need some guidance,{" "}
            <a href="#">see the documentation</a>.
          </p>
        </div>

        <div className="grid grid-cols-2 gap-5">
          <Card title="Create your first resource">
            Create your first resource using{" "}
            <CodeText>python craft collapsar:resource</CodeText>, inside your{" "}
            <CodeText>Resource</CodeText> class, you can customize the way your
            resource is displayed, created, updated and more.
          </Card>
          <Card title="Add fields">
            You can easily manage attributes from your Masonite Model directly
            from Collapsar. You just need whether it is a{" "}
            <CodeText>Text</CodeText>, <CodeText>Select</CodeText>,{" "}
            <CodeText>Image</CodeText> and relax. See all available Fields{" "}
            <a href="#">here</a>.
          </Card>
          <Card title="Customize behaviour">
            Show only the information you want to. Choose which fields are
            displayed in the index, show or edit views.
          </Card>
        </div>
      </div>
    </div>
  );
}

function CodeText({ children }: { children: React.ReactNode }) {
  return <code className="bg-popover rounded-full px-3 py-1">{children}</code>;
}

function Card({ title, content, link, children }: any) {
  return (
    <div className="card bg-secondary p-5 box-border">
      <div className="card-body">
        <h3 className="card-title mb-2 text-xl">{title}</h3>
        <p className="card-text leading-7">{children}</p>
        <div className="mt-5">
          <Button asChild>
            <Link to={link}>Read more</Link>
          </Button>
        </div>
      </div>
    </div>
  );
}
